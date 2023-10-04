import pytest
from api_testing.api_client import ApiClient
from api_testing.api_methods import DogApiServiceClient, OpenBreweryClient, \
    JsonPlaceHolderClient


@pytest.fixture(scope="session")
def client():
    return ApiClient(base_url="https://dog.ceo/api/")


@pytest.fixture
def get_dog():
    return DogApiServiceClient(base_url="https://dog.ceo/api/")


@pytest.fixture(scope="session")
def client_open_brewery():
    return ApiClient(base_url="https://api.openbrewerydb.org/")


@pytest.fixture
def get_postal():
    return OpenBreweryClient(base_url="https://api.openbrewerydb.org/")


@pytest.fixture(scope="session")
def client_json_place_holder():
    return ApiClient(base_url="https://jsonplaceholder.typicode.com/")


@pytest.fixture
def post():
    return JsonPlaceHolderClient(
        base_url="https://jsonplaceholder.typicode.com/")
