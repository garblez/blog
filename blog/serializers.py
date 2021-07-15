from rest_framework import serializers
from blog.models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = ['author', 'content', 'article']