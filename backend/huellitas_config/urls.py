from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Cambiamos admin.site.json por admin.site.urls
    path('admin/', admin.site.urls),
]