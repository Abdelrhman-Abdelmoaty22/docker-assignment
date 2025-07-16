import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get("http://backend:5000")
    return f"Frontend talking to -> {r.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
