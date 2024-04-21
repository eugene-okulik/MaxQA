import requests
import allure

from test_api_mvp1.endpoints.base_endpoint import Endpoint


class UpdateObject(Endpoint):
    @allure.step("Check that object is updated")
    def update_by_id(self, object_id, payload):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=payload)
        self.response_json = self.response.json()

    @allure.step("Check that object id is correct")
    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id, "The id correct"
