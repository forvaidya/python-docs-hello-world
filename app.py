"""
Provides magical app
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """
    Execution::Customery Hello World app.
    """
    return "Hello, World!"
