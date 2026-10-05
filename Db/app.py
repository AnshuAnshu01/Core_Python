from flask import Flask, render_template, request
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/add_manual")
def add_manual():

    name = "anshuman"
    email = "anshumanpanda67@gmail.com"

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

    return "Manual User add Successfully"


@app.route("/delete_user", methods=["POST"])
def delete_user():

    user_id = request.form["id"]

    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = connection.cursor()

    check_query = "SELECT * FROM users WHERE id = %s"

    cursor.execute(check_query, (user_id,))

    user = cursor.fetchone()

    if user is None:

        cursor.close()
        connection.close()

        return "User ID does not exist"

    delete_query = "DELETE FROM users WHERE id = %s"

    cursor.execute(delete_query, (user_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return "User deleted successfully"


@app.route("/delete/<int:user_id>", methods=["GET", "DELETE"])
def delete_user_by_id(user_id):

    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = connection.cursor()

    check_query = "SELECT * FROM users WHERE id = %s"

    cursor.execute(check_query, (user_id,))

    user = cursor.fetchone()

    if user is None:

        cursor.close()
        connection.close()

        return "User ID does not exist"

    delete_query = "DELETE FROM users WHERE id = %s"

    cursor.execute(delete_query, (user_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return "User deleted successfully"


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