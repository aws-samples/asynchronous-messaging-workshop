import boto3
from botocore.config import Config
import json
import os
import random
import time

SERVICE_NAME = os.environ['SERVICE_NAME']
QUEUE_URL = os.environ['QUEUE_URL']

config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 1})
sqs = boto3.client('sqs', config=config)

def i_am_not_available(event):
    return random.choice([True, False])

def lambda_handler(event, context):
    print('{} received event: {}'.format(SERVICE_NAME, json.dumps(event)))

    # we only send a quote, if we are available at that time
    if i_am_not_available(event):
        return

    # if we send a quote, we wait between 0 and 60 seconds to mimic the quote computation
    time.sleep(random.randint(0,60))

    # send the response to the quotes response queue
    message = json.loads(event['Records'][0]['Sns']['Message'])
    response_message = json.dumps({
        'responder': SERVICE_NAME,
        'rfq-id': message['rfq-id'],
        'quote': random.randint(0,100)
    })

    response = sqs.send_message(
        QueueUrl = QUEUE_URL,
        MessageBody = response_message
    )

    print('sent SQS message: {}'.format(response_message))

    return