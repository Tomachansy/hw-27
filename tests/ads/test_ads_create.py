import pytest


@pytest.mark.django_db
def test_ads_create(client, user, category):
    response = client.post(
        '/ad/create/',
        {
            "name": "UserAdName",
            "author": user.id,
            "price": 10,
            "description": "Description",
            "is_published": False,
            "category": category.id
        },
        content_type='application/json')

    assert response.status_code == 201
    assert response.data == {
        "id": 1,
        "name": "UserAdName",
        "author": user.id,
        "price": 10,
        "description": "Description",
        "is_published": False,
        "category": category.id,
        "image": None
    }
