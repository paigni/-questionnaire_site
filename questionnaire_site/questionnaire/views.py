from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from django.views import generic
from questionnaire.models import Question, Choice, Person
from questionnaire.service import is_user_answer


class IndexView(generic.ListView):
    template_name = 'questionnaire/index.html'
    context_object_name = 'latest_question'

    def get_queryset(self):
        return Choice.objects.latest('pub_date')


def vote(request, question_id):

    user = request.session.session_key
    question = get_object_or_404(Question, pk=question_id)
    if is_user_answer(user,question):
        return HttpResponse('Мы вас обязательно спросим о чём то интересном позже')
    else:
        people = Person()
        people.user_id = user
        people.question = question
        people.save()
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponse('Спасибо ваш выбор учтён,вы можете просмотерть статитстику по ссылке')

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionnaire/results.html', {'question': question})
