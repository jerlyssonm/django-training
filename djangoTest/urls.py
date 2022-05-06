from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('api/', include('musicians.urls')),
    path('api/', include('accounts.urls')),
]
