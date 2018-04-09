from django.db import models
from django.utils import  timezone
from django.contrib import admin

# Create your models here.

class News(models.Model):
    title = models.CharField('新闻标题',max_length=200)
    slug = models.CharField('链接后缀',max_length=200)
    source = models.CharField('文章来源',max_length=200,default='http://www.gzxjyiqi.com/')
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    editor = models.CharField('编辑',max_length=200)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField('问题', max_length=200)
    slug = models.CharField('链接后缀', max_length=200)
    source = models.CharField('文章来源', max_length=200, default='http://www.gzxjyiqi.com/')
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    editor = models.CharField('编辑', max_length=200)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

    class Media:
        js = ('/static/js/kindeditor/kindeditor-min.js',
              '/static/js/kindeditor/lang/zh_CN.js',
              '/static/js/kindeditor/config.js',
        )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

    class Media:
        js = ('/static/js/kindeditor/kindeditor-min.js',
              '/static/js/kindeditor/lang/zh_CN.js',
              '/static/js/kindeditor/config.js',
        )

