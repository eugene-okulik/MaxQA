import requests
import allure
from test_api_mvp1.endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step("Get object by id")
    def get_by_id(self, object_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()

    @allure.step("Check that object id is correct")
    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id, "The id correct"
