# coding: utf8
from django import forms
from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if self.cleaned_data['text'].find(u'хуй') > -1:
            raise forms.ValidationError(
                u'Не ругайся, пидор',
                code='spam'
            )

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        if self.cleaned_data['text'].find(u'хуй') > -1:
            raise forms.ValidationError(
                u'Не ругайся, пидор',
                code='spam'
            )

    def save(self):
        self.cleaned_data['question'] = Question.objects.get(id=int(self.cleaned_data['question']))
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
