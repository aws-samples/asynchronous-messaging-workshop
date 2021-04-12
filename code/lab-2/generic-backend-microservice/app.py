import json
import os
import random
import time

SERVICE_NAME = os.environ['SERVICE_NAME']

def process(event):
    print('{} process: {}'.format(SERVICE_NAME, event))
    message_id = event['id']

    # will fail randomly to show the Amazon SNS redelivery feature
    if random.choice([True, False]):
      print("--------------------------------------")
      print("{{'msg-id': '{}', 'status': 'FAILED'}}".format(message_id))
      print("--------------------------------------")
      raise Exception("I'm failing randomly...")

    print("+++++++++++++++++++++++++++++++++++++++++")
    print("{{'msg-id': '{}', 'status': 'PROCESSED'}}".format(message_id))
    print("+++++++++++++++++++++++++++++++++++++++++")


def lambda_handler(event, context):
    print('{} received event: {}'.format(SERVICE_NAME, json.dumps(event)))

    # we set the 'BatchSize' to 1
    request_body = json.loads(event['Records'][0]['body'])
    process(request_body)
