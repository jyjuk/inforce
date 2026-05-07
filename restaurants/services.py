from django.utils import timezone
from .models import Menu


def get_today_menus():
    today = timezone.now().date()
    return (
        Menu.objects.filter(date=today)
        .select_related("restaurant")
        .prefetch_related("items")
    )