from .models import Website_Logo

def website_config(request):
    if Website_Logo.objects.filter(is_active=True).exists():
        website_config = Website_Logo.objects.filter(is_active=True).first()
        return {'website_config': website_config}
    return None
