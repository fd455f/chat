from flask import Flask


app = Flask(__name__)

@app.route("/")
def index(req):
    return "{\"fulfillmentText\": \"Veio do webhook do heroku\", \"followupEventInput\" : {\"name\": \"DesvioWebHook\"}}"

# Wrap Flask app with Talisman
#Talisman(app, content_security_policy=None)

if __name__ == '__main__':
    app.run(debug=False)