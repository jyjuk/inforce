import pytest


@pytest.mark.django_db
def test_admin_can_create_employee(admin_client):
    response = admin_client.post("/api/employees/", {"username": "newworker", "password": "pass123"})
    assert response.status_code == 201


@pytest.mark.django_db
def test_employee_cannot_create_employee(employee_client):
    response = employee_client.post("/api/employees/", {"username": "newworker", "password": "pass123"})
    assert response.status_code == 403
