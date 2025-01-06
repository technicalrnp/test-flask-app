from flask import Flask
 from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World2!</p>"

app.run(port=5000)
