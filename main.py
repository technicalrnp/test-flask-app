from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>this is testing of CICD pipeline using webhooks</p>"

app.run(port=5000)
