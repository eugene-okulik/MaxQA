import requests

BASE_URL = 'https://api.restful-api.dev/objects'


def add_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    headers = {"content-type": "application/json"}

    r = requests.post(BASE_URL, json=payload, headers=headers)

    return r.json()['id']


def put_object():
    id_object = add_object()
    payload = {
        "name": "Apple MacBook Pro 20 NEW",
        "data": {
            "year": 2022,
            "price": 2999.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "1 TB"
        }
    }

    headers = {"content-type": "application/json"}

    r = requests.put(f'{BASE_URL}/{id_object}', json=payload, headers=headers)


def patch_object():
    id_object = add_object()
    payload = {
        "data": {
            "year": 2024,
            "price": 2999.99,
            "CPU model": "Intel Core i12",
            "Hard disk size": "1 TB"
        }
    }

    headers = {"content-type": "application/json"}

    r = requests.patch(f'{BASE_URL}/{id_object}', json=payload, headers=headers)
    print(r.json())

    return r.json()['id']


def delete_object():
    id_object = add_object()

    headers = {"content-type": "application/json"}

    r = requests.delete(f'{BASE_URL}/{id_object}', headers=headers)


delete_object()
