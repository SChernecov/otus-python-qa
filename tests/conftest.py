import pytest
from api_testing.api_client import ApiClient
from api_testing.api_methods import DogApiServiceClient, OpenBreweryClient, \
    JsonPlaceHolderClient


@pytest.fixture(scope="session")
def client():
    client = ApiClient(base_url="https://dog.ceo/api/")
    return client


@pytest.fixture
def get_dog():
    client = DogApiServiceClient(base_url="https://dog.ceo/api/")
    return client


@pytest.fixture(scope="session")
def client_open_brewery():
    client = ApiClient(base_url="https://api.openbrewerydb.org/")
    return client


@pytest.fixture
def get_postal():
    client = OpenBreweryClient(base_url="https://api.openbrewerydb.org/")
    return client


@pytest.fixture(scope="session")
def client_json_place_holder():
    client = ApiClient(base_url="https://jsonplaceholder.typicode.com/")
    return client


@pytest.fixture
def post():
    client = JsonPlaceHolderClient(
        base_url="https://jsonplaceholder.typicode.com/")
    return client
