import os
from pathlib import Path

# BASE_DIR: Define la raíz del proyecto. 
# Para que Django encuentre carpetas como 'media' o 'static'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: En desarrollo, despues cambiar en produccion
SECRET_KEY = 'django-insecure-tu-clave-aqui'
DEBUG = True
ALLOWED_HOSTS = []

# DEFINICIÓN DE APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Librerías para la API 
    'rest_framework',
    'corsheaders',

    # Modulos
    'apps.users',
    'apps.animals',
    'apps.adoptions',
    'apps.events',
    'apps.finance',
]

# MIDDLEWARE: Capas que procesan la petición antes de llegar a tu código.
# Fundamento: 'CorsMiddleware' permite que el programador de Front se conecte.
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'huellitas_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'huellitas_config.wsgi.application'

# BASE DE DATOS: El motor de tu sistema.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'huellitas_db',
        'USER': 'postgres',
        'PASSWORD': 'LKMNMDNAt1.', 
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# IDIOMA Y HORA.
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# ARCHIVOS ESTÁTICOS: Para las fotos de los animales.
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.backends.BigAutoField'

# Permitir que el Frontend (en localhost:3000 o similar) acceda
CORS_ALLOW_ALL_ORIGINS = True