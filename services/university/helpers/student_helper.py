import allure
import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    @allure.step("Post student")
    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response
