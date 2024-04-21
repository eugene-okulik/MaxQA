import requests
import allure

from test_api_mvp1.endpoints.base_endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step("Check that object is created")
    def new_object(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()

    @allure.step("Check that new object is corrected")
    def check_name(self, name):
        assert self.response_json['name'] == name, "The name correct"
