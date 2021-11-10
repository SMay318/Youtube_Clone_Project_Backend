from django.db import models


# Create your models here.
class Comment(models.Model):
    comment = models.TextField(max_length=300)
    videoId = models.TextField(max_length=100)
    likes = models.IntegerField(default=0, null=False)
    dislikes = models.IntegerField(default=0, null=False)
    
    
class Reply(models.Model):    
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.TextField(max_length=300)

    

    