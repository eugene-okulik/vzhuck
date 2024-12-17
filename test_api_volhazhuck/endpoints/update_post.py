import requests
import allure
from endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):

    response = None
    json = None

    @allure.step('Update a post')
    def update_post(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check updated data')
    def check_updated_data(self, key, expected_value):
        response_json = self.response.json()
        assert response_json['data'][key] == expected_value
