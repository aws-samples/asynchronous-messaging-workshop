import json
import os

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
