import pytest

from app import app, items


@pytest.fixture(autouse=True)
def reset_items():
    original_items = list(items)
    yield
    items.clear()
    items.extend(original_items)


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_health_route(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_item(client):
    response = client.post(
        "/add",
        data={
            "name": "Python Book",
            "category": "Books",
            "price": "500",
            "condition": "Good",
            "seller": "Test User",
            "description": "A Python programming book.",
        },
    )

    assert response.status_code == 302
    assert any(item["name"] == "Python Book" for item in items)


def test_invalid_item_rejected(client):
    response = client.post(
        "/add",
        data={
            "name": "",
            "category": "Books",
            "price": "500",
            "seller": "Test User",
        },
    )

    assert response.status_code == 400


def test_mark_sold(client):
    response = client.post("/sell/1")

    assert response.status_code == 302
    assert items[0]["status"] == "Sold"
    
def test_api_items(client):
    response = client.get("/api/items")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)