import requests
import allure
from endpoints.endpoint import Endpoint


class GetPost(Endpoint):

    response = None
    json = None

    @allure.step('Get post by id')
    def get_post(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{post_id}', headers=headers)
        self.json = self.response.json() if self.response else None
        return self.response

    @allure.step('Check post color')
    def check_post_data(self, post_color):
        assert self.json['data']['color'] == post_color

    @allure.step('Check post field')
    def check_post_data_field(self, key, expected_value):
        assert self.json['data'][key] == expected_value
