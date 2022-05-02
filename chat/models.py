from django.db import models

# Create your models here.
class Comment(models.Model):
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)