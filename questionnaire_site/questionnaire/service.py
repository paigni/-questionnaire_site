from .models import Person


def is_new_user(user):
    people = Person.objects.filter(user_id=user)
    if people.exists():
        return False
    else:
        return True


def is_user_answer(user, question):
    people = Person.objects.filter(user_id=user, question_id=question)
    if is_new_user(user):
        return False
    else:
        if people.exists():
            return True
        else:
            return False
