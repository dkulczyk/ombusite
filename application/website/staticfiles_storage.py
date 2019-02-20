import os
from io import BytesIO
from gzip import GzipFile
from django.conf import settings
from django.core.files.base import File, ContentFile
from django.utils.encoding import force_text
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from django.contrib.staticfiles.utils import matches_patterns

SETTINGS = getattr(settings, 'PRECOMPRESSED_SETTINGS', {})
GZIP_PATTERNS = SETTINGS.get('GZIP_PATTERNS', ('*.css', '*.js'))
DEFAULT_COMPRESS_LEVEL = SETTINGS.get('DEFAULT_COMPRESS_LEVEL', 9)

def get_gzipped_name(name):
    """
    returns the location of the gzipped version of a specified file
    """
    file_ext_index = name.rfind('.')
    file_name, file_ext = name[:file_ext_index], name[file_ext_index:]
    return '%s.gz%s' % (file_name, file_ext)

if 'get_gzipped_name' in SETTINGS:
    get_gzipped_name = SETTINGS['get_gzipped_name']

def should_save_gzipped_copy(path):
    """
    returns True if the file specified by path should
    also have a copy gzipped and saved as get_gzipped_name(path)
    """
    return matches_patterns(path, GZIP_PATTERNS)

if 'should_save_gzipped_copy' in SETTINGS:
    should_save_gzipped_copy = SETTINGS['should_save_gzipped_copy']


class SaveGzippedCopyMixin(object):
    """
    SaveGzippedCopyMixin is a class that when used in conjunction
    with a Storage object and STATICFILES_STORAGE augments manage.py's
    collectstatic command to find files that would benefit from gzip
    encoding (by default *.css and *.js files) and saves gzipped
    copies with a modified name (by default *.gz.css and *.gz.js).
    """

    def should_skip_processing(self, source_storage, path, gzipped_name):
        """
        return True if the specified file should not be processed.
        for example, because the processed version already exists
        and is up to date.
        """
        if self.exists(gzipped_name):
            try:
                target_last_modified = self.modified_time(gzipped_name)
                source_last_modified = source_storage.modified_time(path)
                if target_last_modified >= source_last_modified:
                    return True
            except (AttributeError, NotImplementedError, OSError, ValueError):
                pass
        return False

    def pre_save_gzipped(self, name, gzipped_name, pregzipped_file):
        """
        pre_save_gzipped is a hook to allow subclasses to
        alter the pregzipped file's content.
        """
        return pregzipped_file

    def compresslevel(self, name, gzipped_name, pregzipped_file):
        """
        returns the compresslevel for a specified file
        0 is no compression
        1 is the fastest and produces the least compression
        9 is the slowest and produces the most compression
        """
        return DEFAULT_COMPRESS_LEVEL

    def gzipped_file(self, name, gzipped_name, pregzipped_file):
        """
        gzipped_file returns the gzipped version of the specified file.
        """
        gzip_buffer = BytesIO()
        gzipped_file = GzipFile(
            mode='wb',
            compresslevel=self.compresslevel(
                name, gzipped_name, pregzipped_file,
            ),
            fileobj=gzip_buffer,
        )
        gzipped_file.write(pregzipped_file.read())
        gzipped_file.close()
        gzip_buffer.seek(0)
        return File(gzip_buffer)

    def post_save_gzipped(self, name, gzipped_name, gzipped_file):
        """
        post_save_gzipped is a hook to allow subclasses to
        cleanup/further process a gzipped file after it is saved
        """
        pass

    def post_process(self, paths, dry_run=False, **options):
        """
        Post process the given list of files (called from collectstatic).

        Processing finds paths that match the configuration,
        gzips them and copies them to the target storage with
        the name generated by get_gzipped_name.
        """
        # allow other processors to run, yielding their values
        # and adding new files to the list of ones to be gzipped
        if hasattr(super(SaveGzippedCopyMixin, self), 'post_process'):
            processor = super(SaveGzippedCopyMixin, self).post_process(
                paths=paths.copy(), dry_run=dry_run, options=options,
            )
            for original_path, processed_path, processed in processor:
                if processed and original_path != processed_path:
                    paths[processed_path] = (self, processed_path)
                yield original_path, processed_path, processed

        # don't even dare to process the files if we're in dry run mode
        if dry_run:
            return

        path_level = lambda name: len(name.split(os.sep))

        # make a list of files that are to be gzipped
        adjustable_paths = [
            path for path in
            sorted(paths.keys(), key=path_level, reverse=True)
            if should_save_gzipped_copy(path)
        ]

        for name in adjustable_paths:
            storage, path = paths[name]
            gzipped_name = get_gzipped_name(name)
            if not self.should_skip_processing(storage, path, gzipped_name):
                with storage.open(path) as original_file:
                    if hasattr(original_file, 'seek'):
                        original_file.seek(0)
                    pregzipped_file = ContentFile(original_file.read())
                    pregzipped_file = self.pre_save_gzipped(
                        name, gzipped_name, pregzipped_file,
                    )
                    if self.exists(gzipped_name):
                        self.delete(gzipped_name)
                    gzipped_file = self.gzipped_file(
                        name, gzipped_name, pregzipped_file,
                    )
                    saved_name = self._save(gzipped_name, gzipped_file)
                    gzipped_name = force_text(saved_name.replace('\\', '/'))
                    self.post_save_gzipped(
                        name, gzipped_name, gzipped_file,
                    )
                    yield name, gzipped_name, True

class ManifestPrecompressedStaticFilesStorage(SaveGzippedCopyMixin, ManifestStaticFilesStorage):
    pass