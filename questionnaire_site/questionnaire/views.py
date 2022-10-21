from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from questionnaire.models import Question
from questionnaire.forms import UserForm


menu = [{'title': "� �����", 'url_name': 'about'},
        {'title': "���������� �������", 'url_name': 'statistic'}
]

def about(request):
    return render(request, 'index.html', {'menu': menu, 'title': '� �����'})

def statistic(request):
    return render(request, 'index.html', {'menu': menu, 'title': '���������� �������'})

def succes(request):
    return HttpResponse('�� ��� ����������� ������� � ���-�� ���������� �����!')

def index(request):
    if request.method == "POST":
        latest_questionnaire = Question.objects.order_by('-pub_date')[:5]
        template = loader.get_template('polls/index.html')
        context = {
            'latest_questionnaire': latest_questionnaire,
        }
        return HttpResponse(template.render(context, request))



def success(request):
   return HttpResponse('')