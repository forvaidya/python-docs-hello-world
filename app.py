from flask import Flask
"""
Customery Hello World app.
"""

app = Flask(__name__)

@app.route("/")
def hello():
    """
        Execution::Customery Hello World app.
    """
    return "Hello, World!"

