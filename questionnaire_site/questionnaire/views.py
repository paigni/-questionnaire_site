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
    if request.session.get('has_commented', False):
        return HttpResponse("Мы Вас обязательно спросим о чём то интересном позже")
    else:
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'questionnaire/detail.html',
                          {
                              'question': question,
                          })
        else:
            request.session['has_commented'] = True
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponse('Спасибо ваш выбор учтён,вы можете просмотерть статитстику по ссылке')


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionnaire/results.html', {'question': question})
