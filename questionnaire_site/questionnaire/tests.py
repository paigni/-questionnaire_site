from django.test import TestCase
from .service import is_new_user, is_user_answer


class ServiceTest(TestCase):

    def test_is_new_user(self):
        user = 1311
        future_user = is_new_user(user)
        self.assertIs(future_user, True)

    def test_is_user_answer(self):
        user = 1311
        question = 1
        future_answer = is_user_answer(user,question)
        self.assertIs(future_answer, False)
