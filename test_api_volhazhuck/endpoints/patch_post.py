import requests
import allure
from endpoints.endpoint import Endpoint


class PatchPost(Endpoint):

    response = None
    json = None

    @allure.step('Patch a post')
    def patch_post(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            json=body,
            headers=headers
        )
        return self.response

    @allure.step('Check patched data')
    def check_patched_data(self, key, expected_value):
        response_json = self.response.json()
        assert response_json['data'][key] == expected_value
