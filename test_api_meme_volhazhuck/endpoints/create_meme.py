import requests
from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):

    def __init__(self, token_id, url='http://167.172.172.115:52355/meme'):
        self.token = token_id
        self.url = url
        self.response = None
        self.json = None

    def new_meme(self, body):
        headers = {'Authorization': self.token}
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response
