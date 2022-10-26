from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_title = models.CharField(max_length=200,verbose_name="Заголовок")
    question_text = models.CharField(max_length=200,verbose_name="Вопрос")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text