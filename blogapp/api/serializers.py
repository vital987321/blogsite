from blogapp.models import Article, Topic, Comment, User
from rest_framework.serializers import ModelSerializer

class ArticleSerializer(ModelSerializer):
    class Meta:
        model=Article
        fields=['title', 'text', 'topic']

class TopicSerializer(ModelSerializer):
    class Meta:
        model=Topic
        fields=['name', 'description', 'user']

class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields=['text', 'article', 'user']

class UserSerializer():
    model=User
    fields=['username', 'password']