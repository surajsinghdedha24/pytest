from flask import Flask, request, jsonify
import  json

app = Flask(__name__)

@app.get("/Users")
def get_users():
    # Open the JSON file
    with open('user.json') as f:
        data = json.load(f)

    return json.dumps(data)

@app.post("/AddUser")
def add_user():
    user = request.get_json()
    print(user)
    user_list = []
    data = {}
    return_status = 201
    return_text = ''
    with open('user.json','r') as f:
        try:
            user_list = json.load(f)
        except:
            pass

    if user not in user_list:
        user_list.append(user)
        with open('user.json', 'w') as f:
            json.dump(user_list, f)
    else:
        print("User is already present")
        return_status = 400
        return_text = 'User is already present'
    return return_text,return_status

@app.put("/UpdateUser")
def update_user():
    user = request.get_json()
    print(user)
    user_list = []
    data = {}
    return_status = 204
    return_text=''
    with open('user.json','r') as f:
        try:
            user_list = json.load(f)
        except:
            pass

    if user['ID'] in [usr.get('ID') for usr in user_list]:
        for usr in user_list:
            if user['ID'] == usr['ID']:
                usr['Name'] = user['Name']
        with open('user.json', 'w') as f:
            json.dump(user_list, f)
    else:
        print("User is not available")
        return_text = 'User is not available'
        return_status = 404
    return return_text,return_status


@app.delete("/DeleteUser")
def delete_user():
    user = request.get_json()
    print(user)
    user_list = []
    data = {}
    return_status = 204
    return_text=''
    with open('user.json','r') as f:
        try:
            user_list = json.load(f)
        except:
            pass

    if user['ID'] in [usr.get('ID') for usr in user_list]:
        for usr in user_list:
            if user['ID'] == usr['ID']:
                user_list.remove(usr)
        with open('user.json', 'w') as f:
            json.dump(user_list, f)
    else:
        print("User is not available")
        return_text = 'User is not available'
        return_status = 404
    return return_text,return_status

@app.delete("/DeleteAllUsers")
def delete_all_users():
    user = request.get_json()
    print(user)
    user_list = []
    data = {}
    return_status = 204
    return_text=''
    with open('user.json','r') as f:
        try:
            user_list = json.load(f)
        except:
            pass

    user_list.clear()

    with open('user.json', 'w') as f:
        json.dump(user_list, f)

    return return_text,return_status


# driver function
if __name__ == '__main__':
    app.run(debug=True)