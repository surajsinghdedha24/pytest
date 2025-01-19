import json

import pytest
import requests


@pytest.fixture()
def create_user(request):
    def cr_user(url,usr):
        return requests.post(url,
                        data=json.dumps(usr),
                        headers={'Content-Type': 'application/json'})
    return cr_user


@pytest.fixture(scope="session")
def delete_user(request):
    def del_user(url,usr):
        return requests.delete(url,
                        data=json.dumps(usr),
                        headers={'Content-Type': 'application/json'})
    return del_user
