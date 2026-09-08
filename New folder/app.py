from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def Home():
    return 'Hello World'
@app.route('/about')
def About():
    return 'This is the about page'

@app.route('/contact')
def Contact():
    return 'This is the contact page'
@app.route('/submit' , methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "You send data"
    else:
        return "You are only viewing the page"


