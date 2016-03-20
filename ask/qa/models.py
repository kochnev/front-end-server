from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    rating = models.IntegerField(default=1)
    author = models.ForeignKey(User,related_name = 'question_author', null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name = 'question_like')
    def __unicode__(self):
        return self.title
           
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null = True)

class Author(models.Model):
    rating = models.IntegerField()
    name = models.CharField(max_length=50)

class Article(models.Model):
    author = models.ForeignKey(Author)
    text = models.TextField()
    descr = models.TextField(default="adsf")
    
