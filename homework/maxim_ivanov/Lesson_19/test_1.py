import requests
import pytest

import random

BASE_URL = 'https://api.restful-api.dev/objects'


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


@pytest.mark.parametrize('payload', [random_payload() for _ in range(3)])
def test_add_object(payload):
    headers = {"content-type": "application/json"}
    r = requests.post(BASE_URL, json=payload, headers=headers)
    assert r.status_code == 200


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
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def test_put_object(get_id_object):
    headers = {"content-type": "application/json"}
    payload = random_payload()
    r = requests.put(f'{BASE_URL}/{get_id_object}', json=payload, headers=headers)
    assert r.status_code == 200
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
