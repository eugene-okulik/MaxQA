import pytest
from test_api_mvp1.endpoints.create_object import CreateObject
from test_api_mvp1.endpoints.delete_object import DeleteObject


@pytest.fixture()
def object_id(payload):
    create_object = CreateObject()
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_by_id(create_object.response_json['id'])


@pytest.fixture()
def payload():
    return {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
