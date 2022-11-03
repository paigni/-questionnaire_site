from django.contrib import admin

from questionnaire.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question
        fields = [
            'title',
            'text',
            'pub_date'
        ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
