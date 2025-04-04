# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Welcome to New Python App- 04Apr2025-917am"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
