from django.db import models
from django.contrib import admin

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(Blog,BlogAdmin) #设置联合主键（知识点）

