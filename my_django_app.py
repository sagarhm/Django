
import os
from django.conf import settings
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Create a simple view
def index(request):
    return HttpResponse("Hello, world!")

# Initialize the WSGI application
application = get_wsgi_application()

if __name__ == '__main__':
    # Start the Django development server
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
