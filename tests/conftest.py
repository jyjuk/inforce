import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient

from employees.models import Employee
from restaurants.models import Menu, MenuItem, Restaurant


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(username="admin", password="adminpass")


@pytest.fixture
def employee(db):
    user = User.objects.create_user(username="worker", password="pass123")
    return Employee.objects.create(user=user)


@pytest.fixture
def admin_client(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    return api_client


@pytest.fixture
def employee_client(api_client, employee):
    api_client.force_authenticate(user=employee.user)
    return api_client


@pytest.fixture
def restaurant(db):
    return Restaurant.objects.create(name="Test Restaurant")


@pytest.fixture
def today_menu(restaurant):
    menu = Menu.objects.create(restaurant=restaurant, date=timezone.now().date())
    MenuItem.objects.create(menu=menu, name="Borsch", description="Classic", price="4.50")
    return menu
