import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_and_list_transactions():
    client = APIClient()
    # Create user & get token
    client.post(reverse("register"), {"username": "sara", "password": "StrongPass123!"}, format="json")
    token = client.post(reverse("jwt-create"), {"username": "sara", "password": "StrongPass123!"}, format="json").data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    # Create
    resp = client.post("/api/transactions/", {
        "title": "Groceries",
        "amount": "120.50",
        "type": "EXPENSE",
        "date": "2025-01-10",
        "notes": "weekly shopping"
    }, format="json")
    assert resp.status_code == 201

    # List
    resp = client.get("/api/transactions/")
    assert resp.status_code == 200
    assert len(resp.data) == 1
