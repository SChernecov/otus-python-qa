import pytest
from helpers.random_helper import random_punctuations, random_letters, \
    random_whitespaces, random_int, random_bool, random_integer, random_digits


class TestOpenBrewery:
    """Testing https://www.openbrewerydb.org/ service"""

    def test_valid_list_breweries_per_page(self, client_open_brewery):
        random_page_size = random_integer(1, 200)

        r = client_open_brewery.get(path="v1/breweries",
                                    params={
                                        f"per_page": f"{random_page_size}"})
        assert r.status_code == 200, "wrong status code"
        assert len(r.json()) == random_page_size, "wrong len"

    def test_list_breweries_per_page_max_len(self, client_open_brewery):
        r = client_open_brewery.get(path="v1/breweries",
                                    params={"per_page": "201"})
        assert r.status_code == 200, "wrong status code"
        assert len(r.json()) == 200, "wrong page len"

    def test_breweries_by_postal(self, client_open_brewery, get_postal):
        postal = get_postal.get_random_postal()

        r = client_open_brewery.get(path="v1/breweries",
                                    params={"by_postal": f"{postal}"})

        assert r.status_code == 200, "wrong status code"
        if len(r.json()[0]["postal_code"]) == 4:
            assert "-" not in r.json()[0]["postal_code"]
        elif len(r.json()[0]["postal_code"]) > 4:
            assert "-" or "_" in r.json()[0]["postal_code"]

    @pytest.mark.parametrize("postal", [random_punctuations(),
                                        random_letters(),
                                        random_whitespaces(),
                                        random_bool()],
                             ids=["random_punctuations",
                                  "random_letters",
                                  "random_whitespaces",
                                  "random_bool"])
    def test_invalid_breweries_by_postal(self, client_open_brewery, postal):
        r = client_open_brewery.get(path="v1/breweries",
                                    params={"by_postal": f"{postal}"})

        assert r.status_code == 400, "wrong status code"

    @pytest.mark.parametrize("type", [random_punctuations(),
                                      random_letters(),
                                      random_whitespaces(),
                                      random_int(),
                                      random_bool(),
                                      0],
                             ids=["random_punctuations",
                                  "random_letters",
                                  "random_whitespaces",
                                  "random_int",
                                  "random_bool",
                                  "zero"])
    def test_invalid_breweries_by_type(self, client_open_brewery, type):
        r = client_open_brewery.get(path="v1/breweries",
                                    params={"by_type": f"{type}"})

        assert r.status_code == 400, "wrong status code"
        assert r.json() == \
               {'errors': ['Brewery type must include one of these types:'
                           ' ["micro", "nano", "regional", "brewpub", "large",'
                           ' "planning", "bar", "contract", "proprietor",'
                           ' "closed"]']}
