from flask import Flask
app = Flask(__name__)

"""

Customery Hello World app.

"""
@app.route("/")
def hello():
    return "Hello, World!"
