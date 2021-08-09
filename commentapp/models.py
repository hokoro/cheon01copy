from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.SET_NULL,related_name='comment',null = True) #1:many 연결  set null 지우지는 않고 연결되는 게시글이 null 로 초기화 됨 related name : 연결된 이름
    writer = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='comment',null = True)

    #client 한테 댓글 내용만 입력 받으면 됨
    content = models.TextField(null = False)

    created_at = models.DateTimeField(auto_now_add=True) #auto_now add : DB 에 저장되는 순간이 기록된다