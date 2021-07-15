from rest_framework import serializers
from blog.models import Article, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Comment 
        fields = ['author', 'content', 'article']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    #comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'content']
