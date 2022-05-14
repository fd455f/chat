from flask import Flask
from random import choice

app = Flask(__name__)

@app.route("/")
def index():
    if (random.choice([True, False])):
        return "{\"fulfillmentText\": \"Horário não disponível, tente outro.\", \"followupEventInput\" : {\"name\": \"marcar\"}}"
    else:
        return "{\"fulfillmentText\": \"E qual seu nome ?\", \"followupEventInput\" : {\"name\": \"dados\"}}"



if __name__ == '__main__':
    app.run(debug=False)