from rest_framework import serializers
from .models import Comment
from .models import Reply

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment', 'videoId']
        
class ReplySerializer(serializers.ModelSerializer):        
    class Meta: 
        model = Reply
        fields = ['id', 'comment', 'reply']