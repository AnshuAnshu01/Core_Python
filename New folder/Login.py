from flask import Flask,request,redirect,url_for,session,Response
app = Flask(__name__)
#HomePage
@app.route('/' , methods=['GET', 'POST'])
def home():