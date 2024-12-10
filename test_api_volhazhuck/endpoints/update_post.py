import requests
import allure

from endpoints.endpoint import Endpoint

class UpdatePost(Endpoint):

    @allure.step('Update a post')
    def make_changes_in_post(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response
