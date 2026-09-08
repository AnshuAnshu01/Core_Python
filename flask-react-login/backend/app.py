from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
CORS(app)

swagger = Swagger(app)
@app.route("/")
def home():
    return "Server is live"

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "1234":
        return jsonify({
            "success": True,
            "message": "Login successful!"
        })

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    }), 401


if __name__ == "__main__":
    app.run(debug=True)