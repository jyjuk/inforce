from django.contrib.auth.models import User
from .models import Employee


def create_employee(username: str, password: str) -> Employee:
    user = User.objects.create_user(username=username, password=password)
    return Employee.objects.create(user=user)
