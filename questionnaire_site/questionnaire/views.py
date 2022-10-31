from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from django.views import generic
from questionnaire.models import Question, Choice, Person


class IndexView(generic.ListView):
    template_name = 'questionnaire/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:1]


def vote(request, question_id):
    people = Person.objects.all()
    user = request.session.session_key
    Person.user_id = user
    question = get_object_or_404(Question, pk=question_id)
    if Person.user_id in people:
        if question in Person:
            return HttpResponse('index.html')
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponse('Спасибо ваш выбор учтён,вы можете просмотерть статитстику по ссылке')

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionnaire/results.html', {'question': question})
