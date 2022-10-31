from django.contrib import admin
from django import forms

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    pub_date = forms.CharField
    class Meta:
        model = Question
        fieldsets = [
            (None, {'fields': ['question_title']}),
            (None, {'fields': ['question_text']}),
            ('Дата публикации', {'fields': ['pub_date']}),
        ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)