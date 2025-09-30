import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_registration_and_jwt_flow():
    client = APIClient()
    # Register
    resp = client.post(reverse("register"), {"username": "ali", "email": "ali@example.com", "password": "StrongPass123!"}, format="json")
    assert resp.status_code == 201
    # Login
    resp = client.post(reverse("jwt-create"), {"username": "ali", "password": "StrongPass123!"}, format="json")
    assert resp.status_code == 200
    assert "access" in resp.data and "refresh" in resp.data
