import requests
import pytest
import random

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any

BASE_URL = 'https://api.restful-api.dev/objects'


class ObjectData(BaseModel):
    year: int
    price: int
    cpu_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class ObjectDeleted(BaseModel):
    message: str


class ObjectPost(BaseModel):
    id: str
    name: str
    data: ObjectData
    createdAt: datetime


def random_payload():
    return {
        "name": f"Apple MacBook Pro {random.randint(4, 10)}",
        "data": {
            "year": 2019,
            "price": f"{random.randint(2000, 5000)}",
            "CPU model": f"Intel Core i{random.randint(7, 12)}",
            "Hard disk size": "1 TB"
        }
    }


@pytest.fixture(scope="session", autouse=True)
def session_info():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def func_info():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def get_id_object():
    headers = {"content-type": "application/json"}
    payload = random_payload()
    r = requests.post(BASE_URL, json=payload, headers=headers).json()
    post_id = r['id']
    yield post_id
    requests.delete(f'{BASE_URL}/{post_id}')


def get_id_object2():
    headers = {"content-type": "application/json"}
    payload = random_payload()
    r = requests.post(BASE_URL, json=payload, headers=headers).json()
    post_id = r['id']
    return post_id


def delete_object(post_id):
    requests.delete(f'{BASE_URL}/{post_id}')


@pytest.mark.parametrize('payload', [random_payload() for _ in range(3)])
def test_add_object(payload):
    headers = {"content-type": "application/json"}
    r = requests.post(BASE_URL, json=payload, headers=headers)
    assert r.status_code == 200
    ObjectPost(**r.json())


@pytest.mark.parametrize('objectId', [pytest.param(get_id_object2(), marks=pytest.mark.critical),
                                      pytest.param(get_id_object2(), marks=pytest.mark.medium), get_id_object2()])
def test_put_object(objectId):
    headers = {"content-type": "application/json"}
    payload = random_payload()
    r = requests.put(f'{BASE_URL}/{objectId}', json=payload, headers=headers)
    assert r.status_code == 200
    delete_object(objectId)
    print('END')


@pytest.mark.medium
def test_patch_object(get_id_object):
    headers = {"content-type": "application/json"}
    payload = random_payload()
    r = requests.patch(f'{BASE_URL}/{get_id_object}', json=payload, headers=headers)
    assert r.status_code == 200


@pytest.mark.critical
def test_delete_object(get_id_object):
    headers = {"content-type": "application/json"}
    r = requests.delete(f'{BASE_URL}/{get_id_object}', headers=headers)
    assert r.status_code == 200
    print(r.json())
    ObjectDeleted(**r.json())
