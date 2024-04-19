from ..endpoints.create_object import CreateObject
from ..endpoints.delete_object import DeleteObject
from ..endpoints.get_object import GetObject
from ..endpoints.update_object import UpdateObject


def test_create_object(payload):
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_name(payload['name'])
    new_object_endpoint.check_response_is_200()


def test_get_object(object_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(object_id)
    get_object_endpoint.check_response_is_200()
    get_object_endpoint.check_response_id(object_id)


def test_update_object(object_id, payload):
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_by_id(object_id, payload)
    update_object_endpoint.check_response_is_200()
    update_object_endpoint.check_response_id(object_id)


def test_delete_object(object_id):
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_by_id(object_id)
    delete_object_endpoint.check_response_is_200()
