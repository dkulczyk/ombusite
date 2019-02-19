from django.conf import settings

def website_context_processor(request):
    return {
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID
    }
