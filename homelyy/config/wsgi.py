import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Serve media files (dish images) in production via WhiteNoise
# Django's static() helper only works when DEBUG=True, so we need this.
from django.conf import settings
application = WhiteNoise(application, root=str(settings.MEDIA_ROOT), prefix='media')
