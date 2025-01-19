import json

import requests
from pytest import mark

base_url = "http://127.0.0.1:5000/"


def delete_all_user():
    res = requests.delete(base_url + "DeleteAllUsers",
                          data=json.dumps(''),
                          headers={'Content-Type': 'application/json'})
    print(res.status_code)


@mark.parametrize("data, expected, tear_ready", [
    ({"ID": "1", "Name": "Test1"}, {"status": 201, "Response_Text": ""}, {"N"}),
    ({"ID": "1", "Name": "Test1"}, {"status": 400, "Response_Text": "User is already present"}, {"Y"})
])
# @mark.skip
def test_add_user(data, expected, tear_ready, create_user):
    # res =requests.post("http://127.0.0.1:5000/AddUser",
    #               data = json.dumps(data),
    #               headers={'Content-Type': 'application/json'})
    res = create_user(base_url + "AddUser", data)
    assert res.status_code == expected['status']
    assert res.text == expected['Response_Text']
    if tear_ready == "Y":
        delete_all_user()


@mark.skip
@mark.parametrize("data, expected, tear_ready", [
    ({"ID": "1", "Name": "Test 1"}, {"status": 200, "Response_Text": [{"ID": "1", "Name": "Test 1"}]}, {"N"}),
    ({"ID": "2", "Name": "Test2"},
     {"status": 200, "Response_Text": [{"ID": "1", "Name": "Test 1"}, {"ID": "2", "Name": "Test2"}]}, {"Y"})
])
def test_get_list_of_users(data, expected, tear_ready, create_user):
    # base_url = "http://127.0.0.1:5000/"
    res = create_user(base_url + "AddUser", data)
    res = requests.get(base_url + "Users")
    print(res.text)
    assert res.status_code == expected["status"]
    assert res.text == json.dumps(expected["Response_Text"])

    if tear_ready == 'Y':
        delete_all_user()


@mark.parametrize("data, data_update, expected, tear_ready", [
    ({"ID": "1", "Name": "Test1"}, {"ID": "1", "Name": "Test1_1"}, {"status": 204, "Response_Text": ""}, {"N"}),
    ({"ID": "2", "Name": "Test2"}, {"ID": "2", "Name": "Test2_2"}, {"status": 204, "Response_Text": ""}, {"Y"})
])
@mark.skip
def test_update_user(data, data_update, expected, tear_ready, create_user):
    create_user(base_url + "AddUser", data)
    response = requests.put(base_url + "UpdateUser", data=json.dumps(data_update),
                            headers={'Content-Type': 'application/json'})
    assert response.status_code == expected["status"]
    response = requests.get(base_url + "Users")
    print(response.text)

    if tear_ready == 'Y':
        delete_all_user()


@mark.parametrize("data,  expected", [
    ({"ID": "1"}, {"status": 204, "Response_Text": ""}),
    ({"ID": "2"}, {"status": 204, "Response_Text": ""}),
    ({"ID": "2"}, {"status": 404, "Response_Text": "User is not available"})
])
@mark.skip
def test_delete_user(data, expected):
    response = requests.delete(base_url + "DeleteUser", data=json.dumps(data),
                               headers={'Content-Type': 'application/json'})
    assert response.status_code == expected["status"]
    response = requests.get(base_url + "Users")
    print(response.text)
