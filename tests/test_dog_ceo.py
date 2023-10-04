import pytest
from helpers.random_helper import random_punctuations, random_whitespaces, \
    random_int, random_bool


class TestDogCeo:
    """Testing https://dog.ceo/dog-api/ service"""

    def test_random_image(self, client):
        r = client.get(path="breeds/image/random")

        assert r.status_code == 200, "wrong status code"
        assert "message" in r.json(), "message not in response"
        assert r.json()["message"].startswith(
            "https://images.dog.ceo/breeds"), "wrong url in message"
        assert "status" in r.json(), "message not in response"
        assert r.json()["status"] == "success", "wrong status"

    def test_random_images(self, client):
        r = client.get(path="breeds/image/random/3")

        assert r.status_code == 200, "wrong status code"
        assert "message" in r.json(), "message not in response"
        assert r.json()["message"][0].startswith(
            "https://images.dog.ceo/breeds"), "wrong url in message"
        assert r.json()["message"][1].startswith(
            "https://images.dog.ceo/breeds"), "wrong url in message"
        assert r.json()["message"][2].startswith(
            "https://images.dog.ceo/breeds"), "wrong url in message"
        assert len(r.json()["message"]) == 3
        assert "status" in r.json(), "message not in response"
        assert r.json()["status"] == "success", "wrong status"

    def test_all_sub_breeds_list(self, client, get_dog):
        random_breed = get_dog.get_random_breed()

        r = client.get(
            path=f"breed/{random_breed}/images/random")

        assert r.status_code == 200, "wrong status code"
        assert r.json()["message"].startswith(
            f"https://images.dog.ceo/breeds/{random_breed}"), \
            "message not in response"
        assert "status" in r.json(), "wrong url in message"
        assert r.json()["status"] == "success", "wrong status"

    @pytest.mark.parametrize("breed", [random_punctuations(),
                                       random_whitespaces(),
                                       random_int(),
                                       random_bool(),
                                       0],
                             ids=["random_punctuations",
                                  "random_whitespaces",
                                  "random_int",
                                  "random_bool",
                                  "zero"])
    def test_invalid_all_sub_breeds_list(self, client, breed):
        r = client.get(path=f"breed/{breed}/images/random")

        assert r.status_code == 400, "wrong status code"

    @pytest.mark.parametrize("breed", [random_punctuations(),
                                       random_whitespaces(),
                                       random_int(),
                                       random_bool(),
                                       0],
                             ids=["random_punctuations",
                                  "random_whitespaces",
                                  "random_int",
                                  "random_bool",
                                  "zero"])
    def test_invalid_all_sub_breeds_images(self, client, breed):
        r = client.get(path=f"breed/hound/{breed}/images")

        assert r.status_code == 400, "wrong status code"
