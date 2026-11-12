import pytest
import requests


def pytest_addoption(parser):
  parser.addoption(
      "--base-url",
      action="store",
      default="https://jsonplaceholder.typicode.com",
      help="Base URL for the API",
  )


@pytest.fixture(scope="session")
def base_url(request):
  return request.config.getoption("--base-url")


@pytest.fixture(scope="session")
def api_client():
  session = requests.Session()
  yield session
  # Clean up the session after all tests finish
  session.close()