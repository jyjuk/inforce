import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_login_returns_token(api_client):
    User.objects.create_user(username="user1", password="secret123")
    response = api_client.post("/api/auth/login/", {"username": "user1", "password": "secret123"})
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_login_wrong_credentials(api_client):
    response = api_client.post("/api/auth/login/", {"username": "nobody", "password": "wrong"})
    assert response.status_code == 401


@pytest.mark.django_db
def test_token_refresh(api_client):
    User.objects.create_user(username="user2", password="secret123")
    login = api_client.post("/api/auth/login/", {"username": "user2", "password": "secret123"})
    response = api_client.post("/api/auth/refresh/", {"refresh": login.data["refresh"]})
    assert response.status_code == 200
    assert "access" in response.data
