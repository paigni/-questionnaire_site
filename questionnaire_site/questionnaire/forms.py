from django import forms
from .models import Question,Choice


class QuestionForm(forms.Form):
    title = Question.title
    question = Question.text
    pub_date = Question.pub_date
    choice = Choice.text
