from django.urls import path

from . import views
app_name = 'questionnaire'
urlpatterns = [
    path('', views.show_question_and_choice, name='index'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]