from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from django.views import generic
from questionnaire.models import Question, Choice, Person
from .service import is_user_answer,is_new_user


class IndexView(generic.ListView):
    template_name = 'questionnaire/index.html'
    context_object_name = 'latest_question'

    def get_queryset(self):
        return Question.objects.latest('pub_date')


def vote(request, question_id):
    user = request.session.session_key
    question = get_object_or_404(Question, pk=question_id)
    if is_user_answer(user,question):
        return HttpResponse('Мы вас обязательно спросим о чём то интересном позже')
    else:
        if is_new_user(user):
            Person.user_id = user
            Person.question = question
            selected_choice.votes += 1
            selected_choice.save()
        return HttpResponse('Спасибо ваш выбор учтён,вы можете просмотерть статитстику по ссылке')

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionnaire/results.html', {'question': question})
