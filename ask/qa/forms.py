# coding: utf8
from django import forms
from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=80)
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
    text = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, question, *args, **kwargs):
        self.question = question
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data['text'].find(u'хуй') > -1:
            raise forms.ValidationError(
                u'Не ругайся, пидор',
                code='spam'
            )

    def save(self):
        self.cleaned_data['question'] = self.question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
