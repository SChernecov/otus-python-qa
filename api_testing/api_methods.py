import random

import requests
from api_testing.api_client import ApiClient
from helpers.random_helper import random_letters, random_integer


class DogApiServiceClient(ApiClient):

    def __init__(self, base_url):
        super().__init__(base_url)

    def get_random_breed(self):
        breeds = []
        response = self.get(path="breeds/list/all")
        for key, value in enumerate(response.json()["message"]):
            breeds.append(value)
        return random.choices(breeds)[0]


class OpenBreweryClient(ApiClient):

    def __init__(self, base_url):
        super().__init__(base_url)

    def get_random_postal(self):
        postal = []
        response = self.get(path="v1/breweries")
        for value in response.json():
            postal.append(value["postal_code"])
        return random.choice(postal)


class JsonPlaceHolderClient(ApiClient):

    def __init__(self, base_url):
        super().__init__(base_url)

    def create_post(self):
        letters = random_letters()
        integer = random_integer()
        return self.post(path="posts",
                         headers={
                             "Content-type": "application/json;"
                                             " charset=UTF-8"},
                         data={
                             "title": f"{letters}",
                             "body": f"{letters}",
                             "userId": integer,
                         })
