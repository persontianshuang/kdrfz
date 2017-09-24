from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from datetime import datetime

from users.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()

class Book(models.Model):
    raw_name = models.CharField(max_length=2000,primary_key=True)
    # 去掉括号的名字
    simple_name = models.CharField(max_length=2000)

    url = models.CharField(max_length=2000,default='http://')
    img = models.CharField(max_length=2000,default='http://')


    def __str__(self):
        return self.simple_name


class Mark(models.Model):
    user =  models.ForeignKey(User)
    book_from = models.ForeignKey(Book)
    content = models.TextField(max_length=100000)
    find_page = models.CharField(max_length=100)
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




# class ChessBoard(models.Model):
#     board = ArrayField(
#         ArrayField(
#             models.CharField(max_length=10, blank=True),
#             size=8,
#         ),
#         size=8,)
#     def __str__(self):  # __unicode__ on Python 2
#         return str(self.id)
#
# class Dog(models.Model):
#     name = models.CharField(max_length=200)
#     data = JSONField()
#     def __str__(self):  # __unicode__ on Python 2
#         return self.name
