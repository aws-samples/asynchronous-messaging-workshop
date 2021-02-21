import boto3
from botocore.config import Config
import json
import os
import uuid

TABLE_NAME = os.environ['TABLE_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']

config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 1})
dynamodb = boto3.client('dynamodb', config=config)
sns = boto3.client('sns', config=config)

def is_invalid(request):
    # TODO validate all input fields
    # request['from']
    return False

def lambda_handler(event, context):
    print('received event: {}'.format(json.dumps(event)))

    request = json.loads(event['body'])

    if is_invalid(request):
        return {
            'statusCode': 400,
            'body': json.dumps({})
        }

    rfq_id = str(uuid.uuid4())
    request['rfq-id'] = rfq_id

    response = dynamodb.put_item(
        TableName = TABLE_NAME, 
        Item = {
            'id': {'S': request['rfq-id']},
            'responder': {'S': '-'},
            'from': {'S': request['from']},
            'to': {'S': request['to']},
            'customer': {'S': request['customer']}
        }
    )

    response = sns.publish(
        TopicArn = TOPIC_ARN,    
        Message = json.dumps(request),    
    )

    return {
        'statusCode': 201,
        'body': json.dumps({
            "rfq-id": rfq_id
        })
    }