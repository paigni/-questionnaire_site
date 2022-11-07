from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200,verbose_name="Заголовок")
    text = models.CharField(max_length=200,verbose_name="Вопрос")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.text

class Person(models.Model):
    user_id = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
