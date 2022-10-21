from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from questionnaire.models import Question
from questionnaire.forms import UserForm


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Статистика опросов", 'url_name': 'statistic'}
]

def about(request):
    return render(request, 'index.html', {'menu': menu, 'title': 'О сайте'})

def statistic(request):
    return render(request, 'index.html', {'menu': menu, 'title': 'Статистика опросов'})

def succes(request):
    return HttpResponse('Мы вас обязательно спросим о чём-то интересном позже!')

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