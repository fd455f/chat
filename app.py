from flask import Flask
from random import choice


cont=1
app = Flask(__name__)




@app.route("/", methods = ['GET', 'POST'])
def index():
    global cont
    cont =cont +1
    if (cont%2==0):
        return "{\"fulfillmentText\": \"Horário não disponível, tente outro.\", \"followupEventInput\" : {\"name\": \"marcar\"}}"
    else:
        return "{\"fulfillmentText\": \"E qual seu nome ?\", \"followupEventInput\" : {\"name\": \"dados\"}}"



if __name__ == '__main__':
    app.run(debug=False)