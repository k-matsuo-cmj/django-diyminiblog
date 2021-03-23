import datetime
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    name = models.CharField(verbose_name='タイトル', max_length=200)
    description = models.TextField(verbose_name='内容', max_length=2000)
    author = models.ForeignKey('BlogAuthor', verbose_name='著者', on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(verbose_name='投稿日時', default=datetime.datetime.now)

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'
        ordering = ['-post_date']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    

class BlogAuthor(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザ', on_delete=models.SET_NULL, null=True)
    bio = models.TextField(verbose_name='紹介', max_length=1000)

    class Meta:
        verbose_name = '著者'
        verbose_name_plural = 'ブログ著者'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'
    
    def get_absolute_url(self):
        return reverse("blogger-detail", kwargs={"pk": self.pk})


class BlogComment(models.Model):
    description = models.TextField(verbose_name='内容', max_length=1000)
    post_date = models.DateTimeField(verbose_name='投稿日時', default=datetime.datetime.now)
    author = models.ForeignKey(User, verbose_name='著者', on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'ブログコメント'
        ordering = ['post_date']
    
    def __str__(self):
        return str(self.description)[:75]
