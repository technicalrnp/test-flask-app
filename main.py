from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>testingge6g</p>"

app.run(port=5000)
