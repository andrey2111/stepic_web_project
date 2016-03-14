from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, null=True, related_name='question_author')
    likes = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return '/question/%d/' % self.pk

    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return str(self.pk)

    def get_question_url(self):
        return self.question.get_url()

    class Meta:
        db_table = 'answers'

