from django.urls import path

from . import views
app_name = 'questionnaire'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]