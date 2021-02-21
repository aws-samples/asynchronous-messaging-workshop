import json
import os
import random
import requests
import time
from flask import Flask, render_template, request

app = Flask(__name__)
SERVICE_NAME = os.environ["SERVICE_NAME"]

def is_health_ckeck(request):
    return request.method == 'GET'

def is_invalidate_sns_signature(request):
    # TODO: implement the sns signature verification to make sure the message comes from Amazon SNS
    # see https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.verify.signature.html
    return False

def is_subscription_confirmation_request(request):
    return request.method == 'POST' and request.headers.get('x-amz-sns-message-type') == 'SubscriptionConfirmation'

def confirm_subscription(data):
    app.logger.info("\nconfirming subscription: %s", data)
    request_body = json.loads(data)
    subscribe_url = request_body['SubscribeURL']
    requests.get(subscribe_url)
    app.logger.info("subscription confirmed")
    return

@app.route('/', methods=['GET', 'POST'])
def index():
    if is_health_ckeck(request):
        return {'status': 'alive'} , 200

    data = request.get_data(as_text=True)
    app.logger.info("\nprocessing message: %s ...", str(data))

    if is_invalidate_sns_signature(request):
        return {'status': 'invalid signature'}, 500

    if is_subscription_confirmation_request(request):
        confirm_subscription(data)
        return {'status': 'confirmed'} , 200

    message = json.loads(data)['Message']
    message_id = json.loads(message)['id']

    # will fail randomly to show the Amazon SNS redelivery feature
    if random.choice([True, False]):
        app.logger.info("--------------------------------------")
        app.logger.info("{'msg-id': '%s', 'status': 'FAILED'}", message_id)
        app.logger.info("--------------------------------------")
        return {'status': 'error'}, 500
    else:
        app.logger.info("+++++++++++++++++++++++++++++++++++++++++")
        app.logger.info("{'msg-id': '%s', 'status': 'PROCESSED'}", message_id)
        app.logger.info("+++++++++++++++++++++++++++++++++++++++++")
        return {'status': 'processed'}, 200
