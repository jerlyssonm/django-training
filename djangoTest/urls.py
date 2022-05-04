from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aqui informamos referenciamos nossas urls locais
    path('', include('chat.urls')),
    path('api/', include('musicians.urls')),
]
