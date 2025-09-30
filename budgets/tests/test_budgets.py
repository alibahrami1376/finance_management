import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_budget_with_spending():
    client = APIClient()
    # Register & token
    client.post(reverse("register"), {"username": "mona", "password": "StrongPass123!"}, format="json")
    token = client.post(reverse("jwt-create"), {"username": "mona", "password": "StrongPass123!"}, format="json").data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    # Budget
    resp = client.post("/api/budgets/", {
        "title": "Jan Budget",
        "total_amount": "500.00",
        "start_date": "2025-01-01",
        "end_date": "2025-01-31"
    }, format="json")
    assert resp.status_code == 201
    budget_id = resp.data["id"]

    # Expense transaction within budget
    client.post("/api/transactions/", {
        "title": "Rent",
        "amount": "400.00",
        "type": "EXPENSE",
        "date": "2025-01-05"
    }, format="json")

    # Fetch budget again to see computed fields
    resp = client.get(f"/api/budgets/{budget_id}/")
    assert resp.status_code == 200
    assert float(resp.data["spent_amount"]) == 400.0
    assert float(resp.data["remaining_amount"]) == 100.0
    assert resp.data["over_budget"] is False
