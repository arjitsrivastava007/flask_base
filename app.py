# Login App
from flask import Flask, make_response, jsonify, request
import json

app = Flask(__name__)

users = []


@app.route("/login", methods=["GET","POST"])
def ping():
    try:
        payload = json.loads(request.data)
        print(payload)
        if request.method == "POST":

            user_name = payload.get("user_name", None)
            password = payload.get("password", None)
            
            if not user_name:
                return make_response(jsonify({"message": "Missing user_name param"}), 400)
            if not password:
                return make_response(jsonify({"message": "Missing user_name param"}), 400)
            
            user = {
                "user_name": user_name,
                "password": password
            }
            users.append(user)
            return make_response(jsonify({"user": user}), 201)
        else:
            return make_response(jsonify({"users": users}), 200)
    except Exception as err:
        return make_response(jsonify({"error": err}), 500)


if __name__ == '__main__':
    app.run(debug=True)
