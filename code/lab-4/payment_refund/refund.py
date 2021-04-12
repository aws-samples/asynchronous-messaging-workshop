import boto3
import json
import os
import random
import string
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all  # Patch all supported libraries for X-Ray - More info: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html

# Only instrument libraries if not running locally
if "AWS_SAM_LOCAL" not in os.environ:
    patch_all()


class RefundException(Exception):
    def __init__(self, message=None, info=None):
        super(RefundException, self).__init__()
        
        self.message = message or "Refund failed"
        self.details = info or {}


def is_refund_request_valid(refund):
    return all(x in refund for x in ["fareId", "chargeId"])


def lambda_handler(event, context):
    if not is_refund_request_valid(event):
        raise ValueError('Invalid refund request')

    if event['customerId'].endswith('fail_refund'):
        raise RefundException('Forced refund transaction failure', event)

    re = provider_refund(event['chargeId'])

    response = {
        "fareId" : event["fareId"],
        "refundId" : re,
        "chargeId" : event['chargeId']
    }

    return response


def provider_refund(charge_id):
    rand_id = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    return "re_{0}".format(rand_id)
