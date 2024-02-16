import openai
from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)


@app.route('/')
def handle_home():
    return "ok", 200


@app.route("/webhook", methods=['POST'])
def paymentmethod():
    req = request.get_json(silent=True, force=True)
    print(req)
    intent_name = req['queryResult']['intent']['displayName']


    if intent_name == 'paymentmethod':
        parameters = req['queryResult']['parameters']
        card_brand = parameters.get('cardbrand')
        card_number = parameters.get('cardnumber')
        card_expiry_date = parameters.get('cardexpirydate')
        cvv = parameters.get('cvv')

# Generate a random reference number

    reference_number = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=10))

# Prepare the response

    fulfillment_text = {"fulfillmentText": f"Congratulations! Your Payment was successful with reference number {reference_number}. All the information you gave us such as your cardnumber : {card_number} and your CVV will be secured and safe. We wish you a very happy stay."}
    
    return jsonify(fulfillment_text)
