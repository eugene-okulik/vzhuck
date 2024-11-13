import requests


def all_posts():
    response = requests.get('http://167.172.172.115:52353/object').json()
    print(response)


all_posts()


def one_posts():
    response = requests.get('http://167.172.172.115:52353/object').json()
    print(response['data'][0])


one_posts()


def new_post():
    body = {
        "data": {
            "color": "red",
            "size": "small",
        },
        "name": "New 444 object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body, headers=headers
        )
    print(response)
    return response.json()['id']


id = new_post()


def put_a_post():
    body = {
        "data": {
            "color": "red-UPD",
            "size": "small-UPD",
        },
        "name": "New 444 object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{id}',
        json=body, headers=headers
        )
    print(response)
    return response.json()


put_a_post()


def patch_a_post():
    body = {
        "data": {
            "size": "small",
        },
        "name": "New 444 object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{id}',
        json=body, headers=headers
        )
    print(response)
    return response.json()


patch_a_post()


def delete_a_post():
    response = requests.delete(f'http://167.172.172.115:52353/object/{id}')
    print(response.status_code)


delete_a_post()
