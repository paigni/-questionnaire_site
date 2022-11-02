from django.forms import ModelForm
from questionnaire.models import Question,Choice


class ChoiceForm(ModelForm):

    class Meta:
        model = Choice


