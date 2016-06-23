from flask import Flask
from twilio import twiml
import requests
# test

app = Flask(__name__)

path = "http://finance.yahoo.com/webservice/v1/symbols/AAPL/quote?format=json"

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    result = requests.get(path)
    response = twiml.Response()
    price = result.json()['list']['resources'][0]['resource']['fields']['price']
    response.message("The current price of $AAPL is: {0}".format(price))

    return str(response)

if __name__ == "__main__":
    app.debug = True
    app.run()
