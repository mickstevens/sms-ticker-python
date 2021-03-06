from flask import Flask
from flask import request
from twilio import twiml
import requests
# test

app = Flask(__name__)

path = "http://finance.yahoo.com/webservice/v1/symbols/{0}/quote?format=json"


@app.route("/sms", methods=['GET', 'POST'])
def sms():
    response = twiml.Response()
    body = request.form['Body']
    try:
        result = requests.get(path.format(body))
        price = result.json()['list']['resources'][0]['resource']['fields']['price']
        response.message("The current price of {1} is: {0}".format(price, body))
    except:
        response.message("Sorry, we could not find that price.")

    return str(response)

if __name__ == "__main__":
    app.debug = True
    app.run()
