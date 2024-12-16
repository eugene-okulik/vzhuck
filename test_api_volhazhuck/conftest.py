import pytest
import requests
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.delete_post import DeletePost
from endpoints.get_post import GetPost
from endpoints.patch_post import PatchPost


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


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def get_post_endpoint():
    return GetPost()


@pytest.fixture()
def new_post_id():
    create_new_post = CreatePost()
    body = {
        "data": {
            "color": "red",
            "size": "small",
        },
        "name": "New 444 object"
    }
    create_new_post.new_post(body)
    post_id = create_new_post.json['id']
    yield post_id
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
