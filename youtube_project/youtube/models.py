from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.TextField(max_length=300)
    
class Reply(models.Model):    
    reply = models.TextField(max_length=300)
    