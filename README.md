OMBU Website
============

Recommended setup
-----------------

The recommended method is with
[virtualenv](http://www.virtualenv.org/en/latest/index.html). Assuming
virtualenv is installed, this will install this project's dependencies:

    mkvirtualenv ombusite
    workon ombusite
    pip install -r requirements.txt

If pip fails to install requirements, you may need to install pytz separately
using easy_install from within the virtualenv:

    workon ombusite
    easy_install pytz

The v1.3.1 LESS compiler is also required, which can be installed with npm:

    npm install -g less@1.3.1

Build the site
--------------

Using Fabric:

    fab local build

Using the `pelican` command:

    pelican -s config.py -v -r

For debugging purposes, add the -D switch

License
-------

Copyright (c) 2012, OMBU Inc. http://ombuweb.com
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.

- Neither the name of OMBU INC. nor the names of its contributors may be used to
  endorse or promote products derived from this software without specific prior
  written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL OMBU INC. BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

