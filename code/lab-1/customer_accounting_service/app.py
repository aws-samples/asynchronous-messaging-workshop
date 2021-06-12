import json
import random

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    for e in event["Records"]:
    
        message = e["Sns"]["Message"]
        message_id = e["Sns"]["MessageId"]

        # will fail randomly to show the AWS Lambda retry feature
        if random.choice([True, False]):
            print("--------------------------------------")
            logger.info("{'msg-id': '%s', 'status': 'FAILED'}", message_id)
            print("--------------------------------------")
            raise SystemError("Unable to process fare")
        else:
            print("+++++++++++++++++++++++++++++++++++++++++")
            logger.info("{'msg-id': '%s', 'status': 'PROCESSED'}", message_id)
            print("+++++++++++++++++++++++++++++++++++++++++")