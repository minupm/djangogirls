from django.db import models

# Create your models here.
class Feedback(models.Model):
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
