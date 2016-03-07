from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, null=True, related_name='question_author')
    likes = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return str(self.pk)

    class Meta:
        db_table = 'answers'

