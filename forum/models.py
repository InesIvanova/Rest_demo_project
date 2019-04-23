from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone_number = models.IntegerField()


class Question(models.Model):
    author = models.CharField(max_length=200, default='Anonymous')
    question = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')

    def __str__(self):
        return f"{self.author} {self.question}"


class Answer(models.Model):
    author = models.CharField(max_length=200, default='Anonymous')
    content = models.TextField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')


    def __str__(self):
        return f"{self.author} {self.content[:10]}..."



