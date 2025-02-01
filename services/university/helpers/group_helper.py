import allure
import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    @allure.step("Post group")
    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response
