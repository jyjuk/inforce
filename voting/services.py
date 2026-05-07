from django.utils import timezone
from django.db.models import Count
from rest_framework.exceptions import ValidationError

from employees.models import Employee
from restaurants.models import Menu
from .models import Vote


def cast_vote(employee: Employee, menu_id: int) -> Vote:
    today = timezone.now().date()

    if Vote.objects.filter(employee=employee, date=today).exists():
        raise ValidationError("You have already voted today.")

    try:
        menu = Menu.objects.get(id=menu_id, date=today)
    except Menu.DoesNotExist:
        raise ValidationError("Menu not found or not available today.")

    return Vote.objects.create(employee=employee, menu=menu)


def get_today_results():
    today = timezone.now().date()
    return (
        Menu.objects.filter(date=today)
        .annotate(vote_count=Count("votes"))
        .select_related("restaurant")
        .order_by("-vote_count")
    )
