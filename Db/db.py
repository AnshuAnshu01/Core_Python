from flask import Flask, request
import pymysql
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

    return """
    <html>
    <body>
        <h2>Add User</h2>

        <form method="POST">

            <label>Name:</label>
            <input type="text" name="name" required>
            <br><br>

            <label>Email:</label>
            <input type="email" name="email" required>
            <br><br>

            <button type="submit">Add User</button>

        </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)