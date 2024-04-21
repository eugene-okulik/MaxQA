from locust import HttpUser, task, between

import random


class JSONPlaceholder(HttpUser):
    wait_time = between(1, 5)

    def random_payload(self):
        return {
            'title': 'foo',
            'body': 'bar',
            'userId': 1,
        }

    @task(2)
    def get_posts(self):
        self.client.get("/posts")

    @task(1)
    def get_post(self):
        self.client.get(f"/posts/{random.randint(1, 99)}")

    @task(1)
    def get_comments_for_post(self):
        self.client.get(f"/posts/{random.randint(1, 99)}/comments")

    @task(1)
    def add_post(self):
        self.client.post("/posts", json=self.random_payload())
