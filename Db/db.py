from flask import Flask, render_template, request
import pymysql  # pyright: ignore[reportMissingImports]  # type: ignore[import-not-found]
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor()

        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))

        connection.commit()

        cursor.close()
        connection.close()

        return "User added successfully"

    return render_template("index.html")

@app.route("/base", methods=["GET"])
def users():

    return render_template("base.html")

@app.route("/reg", methods=["GET"])
def register():
    return render_template("reg.html")

if __name__ == "__main__":
    app.run(debug=True)