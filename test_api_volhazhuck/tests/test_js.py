import requests
import pytest
from endpoints.endpoint import Endpoint

TEST_DATA = [
    {"data": {"color": "peach", "size": "small"}, "name": "9 December obj"},
    {"data": {"color": "pink", "size": "huge"}, "name": "pig"}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_post_create(create_post_endpoint, data):
    # with allure.step('Prepare test data'):
    #     body = {
    #         "data": {
    #             "color": "peach",
    #             "size": "small",
    #         },
    #         "name": "New 9 dec object"
    #     }
        #headers = {'Content-Type': 'application/json'}
    # response = requests.post(
    #     'http://167.172.172.115:52353/object',
    #     json=body, headers=headers
    # )
    #create_endpoint = CreatePost()

    create_post_endpoint.new_post(body=data)
    create_post_endpoint.check_status_200()  
    response = create_post_endpoint.json
    

    #assert response.status_code == 200
    #response_json = create_endpoint.json

    post_id = response['id']
    udated_responce = requests.get(
        f'http://167.172.172.115:52353/object/{post_id}'
    ).json()
    assert udated_responce['data']['color'] == data['data']['color']



def test_put_a_post(update_post_endpoint):
    body = {
        "data": {
            "color": "UPD color",
            "size": "UPD size",
        },
        "name": "New 444 object"
    }
    headers = {'Content-Type': 'application/json'}
    # response = requests.put(
    #     f'http://167.172.172.115:52353/object/{new_post_id}',
    #     json=body, headers=headers
    # )

    update_post_endpoint.make_changes_in_post(post_id, body) #id?
    update_post_endpoint.check_status_200()  
    udated_responce = requests.get(
        f'http://167.172.172.115:52353/object/{post_id}'
    ).json()
    assert udated_responce['data']['color'] == "UPD color"
    assert udated_responce['data']['size'] == "UPD size"

# def test_post_create():
#     body = {
#         "data": {
#             "color": 'red',
#             "size": "small",
#         },
#         "name": "New 4 dec object"
#     }
#     headers = {'Content-Type': 'application/json'}
#     create_endpoint = CreatePost()
#     create_endpoint.new_post(body=body, headers=headers)
#     response = create_endpoint.json
   
#     # post_id = response.json()['id']
#     assert response.status_code == 404
#     # udated_responce = requests.get(
#     #     f'http://167.172.172.115:52353/object/{post_id}'
#     # ).json()
#     #assert response['data']['color'] == 'red'
