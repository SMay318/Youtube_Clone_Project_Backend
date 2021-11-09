from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Comment(models.Model):
    comment = models.TextField(max_length=300)
    videoId = models.TextField(max_length=100)
    
    
class Reply(models.Model):    
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField(max_length=300)

    

    