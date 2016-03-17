# coding: utf8
from django import forms
from models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self._user = None
        super(AskForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data['text'].find(u'хуй') > -1:
            raise forms.ValidationError(
                u'Не ругайся, пидор',
                code='spam'
            )

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        self._user = None
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data['text'].find(u'хуй') > -1:
            raise forms.ValidationError(
                u'Не ругайся, пидор',
                code='spam'
            )

    def save(self):
        self.cleaned_data['author'] = self._user
        self.cleaned_data['question'] = Question.objects.get(id=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignUpForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
            raise forms.ValidationError("this user exist already")
        except User.DoesNotExist:
            return self.cleaned_data['username']

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user
