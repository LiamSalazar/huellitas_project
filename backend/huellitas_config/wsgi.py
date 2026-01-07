import os
from django.core.wsgi import get_wsgi_application

# Establece el módulo de configuración por defecto para el programa 'django'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'huellitas_config.settings')

# Esta es la variable 'application' que el error decía que no encontraba
application = get_wsgi_application()