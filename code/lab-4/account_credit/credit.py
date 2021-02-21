import boto3
import json
import os
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all  # Patch all supported libraries for X-Ray - More info: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html

# Only instrument libraries if not running locally
if 'AWS_SAM_LOCAL' not in os.environ:
    patch_all()


class AccountCreditException(Exception):
    def __init__(self, message=None, info=None):
        super().__init__(message)

        self.message = message or 'Account credit failed'
        self.details = info or {}


def is_credit_request_valid(credit):
    return all(x in credit for x in ['customerId', 'chargeId'])


def lambda_handler(event, context):
    if not is_credit_request_valid(event):
        raise ValueError('Invalid credit request')

    if event['customerId'].endswith('fail_credit'):
        raise AccountCreditException('Forced account credit transaction failure', event)

    return event
