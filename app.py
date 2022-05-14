from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=False)