import boto3
from botocore.config import Config
import json
import os

TABLE_NAME = os.environ['TABLE_NAME']

config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 1})
dynamodb = boto3.client('dynamodb', config=config)

def lambda_handler(event, context):
    print('received event: {}'.format(json.dumps(event)))

    # we configured the event source to only receive one message at a time
    msg = json.loads(event['Records'][0]['body'])

    # store the received response message in our DynamoDB table for the given rfq-id
    response = dynamodb.put_item(
        TableName = TABLE_NAME, 
        Item = {
            'id': {'S': msg['rfq-id']},
            'responder': {'S': msg['responder']},
            'quote': {'N': str(msg['quote'])}
        }
    )

    return