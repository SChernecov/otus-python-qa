import pytest
import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, **kwargs):
        response = self.session.get(url=self.base_url + path, **kwargs)
        return response

    def post(self, path, **kwargs):
        response = self.session.post(url=self.base_url + path, **kwargs)
        return response

    def delete(self, path, **kwargs):
        response = self.session.delete(url=self.base_url + path, **kwargs)
        return response
