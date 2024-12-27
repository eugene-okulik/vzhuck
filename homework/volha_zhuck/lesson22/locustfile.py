from locust import task, HttpUser
import random


class ApiUser(HttpUser):

    @task(1)
    def get_all_posts(self):
        self.client.get(
            '/object'
        )

    @task(3)
    def get_one_post(self):
        self.client.get(
            f'/object/{random.choice([1900, 1218, 1219])}'
        )
