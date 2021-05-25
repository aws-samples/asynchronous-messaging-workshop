import boto3
from botocore.config import Config
import json
import os
import uuid

TABLE_NAME = os.environ['TABLE_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']

config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 1})
dynamodb = boto3.client('dynamodb', config=config)
# sns = boto3.client('sns', config=config)

def is_invalid(request):
    # TODO: validate request
    return False

def lambda_handler(event, context):
    print('EVENT: {}'.format(json.dumps(event)))

    request = json.loads(event['body'])
    print('The request loaded ' + str(request))

    if is_invalid(request):
        return {
            'statusCode': 400,
            'body': json.dumps({})
        }

    print('Request is valid!')

    id = str(uuid.uuid4())
    request['id'] = id

    response = dynamodb.put_item(
        TableName=TABLE_NAME,
        Item={
            'id': {'S': id},
            'from': {'S': request['from']},
            'to': {'S': request['to']},
            'duration': {'N': str(request['duration'])},
            'distance': {'N': str(request['distance'])},
            'customer': {'S': request['customer']},
            'fare': {'N': str(request['fare'])}
        }
    )

    # response = sns.publish(
    #     TopicArn=TOPIC_ARN,
    #     Message=json.dumps(request),
    #     MessageAttributes = {
    #         'fare': {
    #            'DataType': 'Number',
    #            'StringValue': str(request['fare'])
    #         },
    #         'distance': {
    #            'DataType': 'Number',
    #            'StringValue': str(request['distance'])
    #         }
    #    }
    # )

    return {
        'statusCode': 201,
        'body': json.dumps({
            "id": id
        })
    }
