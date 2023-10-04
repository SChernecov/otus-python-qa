import pytest
from helpers.random_helper import random_punctuations, random_letters, \
    random_whitespaces, random_int, random_bool


class TestJsonPlaceHolder:
    """Testing https://jsonplaceholder.typicode.com/ service"""

    def test_get_all_posts(self, client_json_place_holder):
        r = client_json_place_holder.get(path="posts")

        assert r.status_code == 200, "wrong status code"
        assert any("userId" in _ for _ in r.json()), "userId not in response"
        assert any("id" in _ for _ in r.json()), "id not in response"
        assert any("title" in _ for _ in r.json()), "title not in response"
        assert any("body" in _ for _ in r.json()), "body not in response"

    def test_get_posts(self, client_json_place_holder):
        number = random_int()

        r = client_json_place_holder.get(path=f"posts/{number}")

        assert r.status_code == 200, "wrong status code"
        assert r.json()["id"] == number, "wrong id"
        assert "userId" in r.json(), "userId not in response"
        assert "title" in r.json(), "title not in response"
        assert "body" in r.json(), "body not in response"

    @pytest.mark.parametrize("number", [random_punctuations(),
                                        random_letters(),
                                        random_whitespaces(),
                                        random_bool()],
                             ids=["random_punctuations",
                                  "random_letters",
                                  "random_whitespaces",
                                  "random_bool"])
    def test_invalid_get_posts(self, client_json_place_holder, number):
        r = client_json_place_holder.get(path=f"posts/{number}")

        assert r.status_code == 400, "wrong status code"

    @pytest.mark.parametrize("post_id", [random_punctuations(),
                                         random_letters(),
                                         random_whitespaces(),
                                         random_bool()],
                             ids=["random_punctuations",
                                  "random_letters",
                                  "random_whitespaces",
                                  "random_bool"])
    def test_invalid_get_comments_by_post_id(self, client_json_place_holder,
                                             post_id):
        r = client_json_place_holder.get(path=f"comments",
                                         params={"postId": f"{post_id}"})

        assert r.status_code == 400, "wrong status code"

    def test_post_posts(self, post):
        r = post.create_post()

        assert r.status_code == 200, "wrong status code"
