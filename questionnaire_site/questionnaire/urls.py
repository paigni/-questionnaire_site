from django.urls import path
from questionnaire import views

urlpatterns = [
    path('', views.show_question_and_choice, name='index'),
    path('vote/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
]