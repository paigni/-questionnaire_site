from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from questionnaire.models import Question, Choice, Person
from questionnaire.service import is_user_answer


def show_question_and_choice(request):
    question = Question.objects.latest('pub_date')
    latest_question_id = question.id
    user = request.session.session_key
    if not is_user_answer(user, latest_question_id) and request.method == "GET":
        template_name = 'questionnaire/index.html'
        choices = Choice.objects.filter(question_id=latest_question_id )
        return render(request, template_name, {'question': question, 'choices': choices})
    else:
        return HttpResponseRedirect('/vote/')


def vote(request):
    template_name = 'questionnaire/detail.html'
    user = request.session.session_key
    question = Question.objects.latest('pub_date')
    latest_question_id = question.id
    if is_user_answer(user, latest_question_id) and request.method == 'GET':
        return HttpResponse('Мы вас обязательно спросим о чём то интересном позже')
    else:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        people = Person()
        people.user_id = user
        people.question = question
        people.save()
        selected_choice.vote +=1
        selected_choice.save()
        return render(request,template_name)


def results(request):
    template_name = 'questionnaire/results.html'
    question = Question.objects.latest('pub_date')
    return render(request, template_name, {'question': question})
