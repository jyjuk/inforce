import pytest


@pytest.mark.django_db
def test_admin_cannot_vote_without_employee_profile(admin_client, today_menu):
    response = admin_client.post("/api/voting/", {"menu_id": today_menu.id})
    assert response.status_code == 403


@pytest.mark.django_db
def test_employee_can_vote(employee_client, today_menu):
    response = employee_client.post("/api/voting/", {"menu_id": today_menu.id})
    assert response.status_code == 201


@pytest.mark.django_db
def test_cannot_vote_twice(employee_client, today_menu):
    employee_client.post("/api/voting/", {"menu_id": today_menu.id})
    response = employee_client.post("/api/voting/", {"menu_id": today_menu.id})
    assert response.status_code == 400


@pytest.mark.django_db
def test_results_v1_returns_winner(employee_client, today_menu, employee):
    employee_client.post("/api/voting/", {"menu_id": today_menu.id})
    response = employee_client.get("/api/voting/results/")
    assert response.status_code == 200
    assert "restaurant" in response.data
    assert response.data["votes"] == 1


@pytest.mark.django_db
def test_results_v2_returns_list(employee_client, today_menu, employee):
    employee_client.post("/api/voting/", {"menu_id": today_menu.id})
    response = employee_client.get("/api/voting/results/", HTTP_BUILD_VERSION="2")
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert response.data[0]["votes"] == 1
