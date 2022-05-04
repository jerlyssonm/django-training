from django.urls import path
from .views import MusicianView

urlpatterns = [
    path('musicians/', MusicianView.as_view()),
    path('musicians/<int:musician_id>/', MusicianView.as_view())
]