import allure


class Endpoint:
    response = None
    response_json = None

    @allure.step("Check that response is 200")
    def check_response_is_200(self):
        assert self.response.status_code == 200, "The response code is 200"
