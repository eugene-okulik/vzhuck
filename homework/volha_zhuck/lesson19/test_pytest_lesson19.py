import requests
import pytest


@pytest.fixture()
def new_post_id():
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
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


@pytest.fixture(scope='function', autouse=True)
def before_after():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='session', autouse=True)
def start_end():
    print('Start testing')
    yield
    print('Testing completed')


def test_get_all_posts():
    print('test1')
    response = requests.get('http://167.172.172.115:52353/object').json()
    assert len(response) == 1


def test_one_posts(new_post_id):
    print(f'http://167.172.172.115:52353/object/{new_post_id}')
    response = requests.get(f'http://167.172.172.115:52353/object/{new_post_id}').json()
    assert response['id'] == new_post_id


@pytest.mark.parametrize('color', ['yellow', '       ', 'f9999'])
def test_post_create(color):
    body = {
        "data": {
            "color": color,
            "size": "small",
        },
        "name": "New 66 object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body, headers=headers
    )
    post_id = response.json()['id']
    assert response.status_code == 200
    udated_responce = requests.get(
        f'http://167.172.172.115:52353/object/{post_id}'
    ).json()
    assert udated_responce['data']['color'] == color


def test_put_a_post(new_post_id):
    body = {
        "data": {
            "color": "UPD color",
            "size": "UPD size",
        },
        "name": "New 444 object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_post_id}',
        json=body, headers=headers
    )
    assert response.status_code == 200
    udated_responce = requests.get(
        f'http://167.172.172.115:52353/object/{new_post_id}'
    ).json()
    assert udated_responce['data']['color'] == "UPD color"
    assert udated_responce['data']['size'] == "UPD size"


@pytest.mark.medium
def test_patch_a_post(new_post_id):
    body = {
        "data": {
            "size": "large",
        },
        "name": "New 444 object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_post_id}',
        json=body, headers=headers
    )
    assert response.status_code == 200
    udated_responce = requests.get(
        f'http://167.172.172.115:52353/object/{new_post_id}'
    ).json()
    assert udated_responce['data']['size'] == "large"


@pytest.mark.critical
def test_delete_a_post(new_post_id):
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{new_post_id}'
    )
    assert response.status_code == 200
    new_response = requests.get(
        f'http://167.172.172.115:52353/object/{new_post_id}'
    )
    assert new_response.status_code == 404
