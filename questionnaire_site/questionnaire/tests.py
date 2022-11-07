from django.test import TestCase
from questionnaire.service import is_user_answer
from questionnaire.models import Person,Question


class ServiceTest(TestCase):

    def test_is_user_answer(self):
        ques = Question()
        ques.text = '131'
        ques.title = '3131'
        ques.save()

        people = Person()
        people.user_id = 1311
        people.question_id = 1
        people.save()

        user = 1311
        question = 1
        future_answer = is_user_answer(user,question)
        self.assertTrue(future_answer)

        user = 1312
        question = 1
        future_answer = is_user_answer(user, question)
        self.assertFalse(future_answer)

