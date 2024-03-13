from django.contrib import admin
from blogapp.models import Article, Topic, Comment, User

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(Comment)
