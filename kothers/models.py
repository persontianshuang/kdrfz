
# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from datetime import datetime

from users.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()


class Mark(models.Model):
    user =  models.ForeignKey(User)
    # weixin zhihu
    tag_from = models.CharField()
    # 如果有的话  来源url
    find_url = models.CharField(max_length=10000,default='http://')

    content = models.TextField(max_length=100000)

    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self. content[:50]

class Note(models.Model):
    # default=User.objects.filter(id =1)[0]
    user =  models.ForeignKey(User)
    mark_from = models.ForeignKey(Mark)
    content = models.TextField(max_length=100000)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content[:50]

class Comment(models.Model):
    user =  models.ForeignKey(User)
    mark_from = models.ForeignKey(Mark)
    content = models.TextField(max_length=100000)
    add_time = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.content[:50]
