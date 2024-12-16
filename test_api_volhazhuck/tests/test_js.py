import pytest


TEST_DATA = [
    {"data": {"color": "peach", "size": "small"}, "name": "9 December obj"},
    {"data": {"color": "pink", "size": "huge"}, "name": "pig"}
]

UPDATED_DATA = [
    {"data": {"color": "WHITE", "size": "XXL"}, "name": "TOP"},
]


def test_one_posts(new_post_id, get_post_endpoint):
    get_post_endpoint.get_post(new_post_id)
    get_post_endpoint.check_status_200()
    assert get_post_endpoint.json['id'] == new_post_id


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_create(create_post_endpoint, data, get_post_endpoint):
    create_post_endpoint.new_post(body=data)
    create_post_endpoint.check_status_200()
    post_id = create_post_endpoint.post_id
    get_post_endpoint.get_post(post_id)
    get_post_endpoint.check_post_data(data['data']['color'])


def test_patch_a_post(new_post_id, patch_post_endpoint, get_post_endpoint):
    updated_data = {"data": {"color": "blue"}}
    patch_post_endpoint.patch_post(post_id=new_post_id, body=updated_data)
    patch_post_endpoint.check_status_200()
    get_post_endpoint.get_post(new_post_id)
    get_post_endpoint.check_post_data(updated_data['data']['color'])


def test_update_post(new_post_id, update_post_endpoint, get_post_endpoint):
    updated_data = UPDATED_DATA[0]
    update_post_endpoint.update_post(post_id=new_post_id, body=updated_data)
    update_post_endpoint.check_status_200()
    get_post_endpoint.get_post(new_post_id)
    get_post_endpoint.check_post_data_field(
        'color', updated_data['data']['color']
    )
    get_post_endpoint.check_post_data_field(
        'size', updated_data['data']['size']
    )
    assert get_post_endpoint.json['name'] == updated_data['name']


def test_delete_post(new_post_id, delete_post_endpoint, get_post_endpoint):
    delete_post_endpoint.delete_post(new_post_id)
    delete_post_endpoint.check_status_200()
    get_post_endpoint.get_post(new_post_id)
    get_post_endpoint.check_status_404
