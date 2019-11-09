import boto3
from botocore.config import Config
import json
import os

TABLE_NAME = os.environ['TABLE_NAME']

config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 1})
dynamodb = boto3.client('dynamodb', config=config)

def assemble(response):
    body = {
        'quotes': []
    }

    for item in response['Items']:
        if 'quote' in item:
            body['quotes'].append({
                'responder': item['responder']['S'],
                'quote': item['quote']['N']
            })
        else:
            body['rfq-id'] = item['id']['S']
            body['from'] = item['from']['S']
            body['to'] = item['to']['S']
            body['customer'] = item['customer']['S']

    return body

def lambda_handler(event, context):
    print('received event: {}'.format(json.dumps(event)))
    id = event['pathParameters']['id']

    # query DynamoDB with the rfq-id provided in the request
    response = dynamodb.query(
        TableName = TABLE_NAME,
        KeyConditionExpression = 'id = :id',
        ExpressionAttributeValues = {':id': {'S': id}}
    )

    body = assemble(response)

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }