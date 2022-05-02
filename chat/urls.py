from django.urls import path
from .views import CommentView


# relacionando a url com a view
urlpatterns = [
    path('comment/<int:comment_id>/', CommentView.as_view()),
    path('comment/', CommentView.as_view())
]