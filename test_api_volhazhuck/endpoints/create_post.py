import requests
import allure
from endpoints.endpoint import Endpoint

class CreatePost(Endpoint):

    @allure.step('Create new post')
    def new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

