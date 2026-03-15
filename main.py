from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>testing 74</p>"

app.run(port=5000)
