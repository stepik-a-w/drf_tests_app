import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stepic_drf_tests.settings')

application = get_wsgi_application()
