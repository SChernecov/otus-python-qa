import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", default="https://ya.ru", type=str, help="Choose url"
    )

    parser.addoption(
        "--status_code", default=200, type=int, help="Status code"
    )


@pytest.fixture
def actual(request):
    return request.config.getoption("--url")


@pytest.fixture
def expected(request):
    return request.config.getoption("--status_code")
