import requests
import allure

from test_api_mvp1.endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step("Check that object is deleted")
    def delete_by_id(self, object_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()
