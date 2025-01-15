import pytest
import requests
from endpoints.create_meme import CreateMeme
from endpoints.get_meme import GetMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.put_meme import PutMeme


@pytest.fixture()
def get_meme_endpoint(get_token):
    return GetMeme(get_token)


@pytest.fixture()
def get_all_memes_endpoint(get_token):
    return GetMeme(get_token)


@pytest.fixture()
def delete_meme_endpoint(get_token):
    return DeleteMeme(get_token)


@pytest.fixture()
def create_meme_endpoint(get_token):
    return CreateMeme(get_token)


@pytest.fixture()
def update_meme_endpoint(get_token):
    return PutMeme(get_token)


@pytest.fixture()
def update_meme_data(get_token):
    return PutMeme(get_token)


@pytest.fixture(scope='session', autouse=True)
def get_token():
    url = 'http://167.172.172.115:52355/authorize'
    body = {"name": "olga"}
    response = requests.post(url, json=body)
    response = response.json()
    token_id = response['token']
    return token_id


@pytest.fixture()
def update_meme_data():
    def generate_updated_data(new_meme_id):
        return {
            "id": new_meme_id,
            "info": {
                "colors": ["green"],
                "objects": ["picture", "text"]
            },
            "tags": ["fun", "grinch"],
            "text": "Grinch",
            "updated_by": "olga",
            "url": "https://encrypted-tbn0"
        }
    return generate_updated_data


@pytest.fixture()
def new_meme_id(get_token):
    body = {
        "info": {
            "colors": [
                "purple"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "grinch"
        ],
        "text": "Grinch",
        "updated_by": "olga",
        "url": "https://encrypted-tbn0"
    }
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=body, headers={
            'Content-Type': 'application/json',
            'Authorization': get_token}
    )
    meme_id = response.json()['id']
    yield meme_id
    requests.delete(
        f'http://167.172.172.115:52355/meme/{meme_id}',
        headers={'Authorization': get_token}
    )
