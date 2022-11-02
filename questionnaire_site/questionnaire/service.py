from questionnaire.models import Person


def is_user_answer(user, question):
    people = Person.objects.filter(user_id=user, question_id=question)
    if people.exists():
        return True
    else:
        return False
