import pytest
from django.utils import timezone


@pytest.mark.django_db
def test_admin_can_create_restaurant(admin_client):
    response = admin_client.post("/api/restaurants/", {"name": "New Place"})
    assert response.status_code == 201


@pytest.mark.django_db
def test_employee_cannot_create_restaurant(employee_client):
    response = employee_client.post("/api/restaurants/", {"name": "New Place"})
    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_upload_menu(admin_client, restaurant):
    payload = {
        "restaurant": restaurant.id,
        "date": timezone.now().date().isoformat(),
        "items": [{"name": "Soup", "description": "Hot soup", "price": "3.50"}],
    }
    response = admin_client.post("/api/restaurants/menu/", payload, format="json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_today_menu_list(employee_client, today_menu):
    response = employee_client.get("/api/restaurants/menu/today/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["restaurant"] == today_menu.restaurant.id
