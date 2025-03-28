import pytest


TEST_DATA = [
    {"info": {"colors": ["green"], "objects": ["picture", "text"]},
        "tags": ["fun", "grinch"], "text": "Grinch",
        "updated_by": "olga",
        "url": "https://encrypted-tbn0"}
]


def test_get_all_memes(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes()
    get_all_memes_endpoint.check_status_200()


def test_get_one_meme(new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme(new_meme_id)
    get_meme_endpoint.check_status_200()
    assert get_meme_endpoint.json['id'] == new_meme_id


def test_delete_meme(new_meme_id, delete_meme_endpoint, get_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_status_200()
    get_meme_endpoint.get_meme(new_meme_id)
    get_meme_endpoint.check_status_404()


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_new_meme(create_meme_endpoint, data, get_meme_endpoint):
    create_meme_endpoint.new_meme(body=data)
    create_meme_endpoint.check_status_200()
    meme_id = create_meme_endpoint.meme_id
    get_meme_endpoint.get_meme(meme_id)
    get_meme_endpoint.check_meme_data(data['info']['colors'])


def test_put_a_post(
        new_meme_id, get_meme_endpoint,
        update_meme_endpoint, update_meme_data):
    updated_data = update_meme_data(new_meme_id)
    get_meme_endpoint.get_meme(new_meme_id)
    get_meme_endpoint.check_status_200()
    update_meme_endpoint.put_meme(meme_id=new_meme_id, body=updated_data)
    update_meme_endpoint.check_status_200()
    get_meme_endpoint.get_meme(new_meme_id)
    assert get_meme_endpoint.json[
        'info']['colors'] == updated_data['info']['colors']
