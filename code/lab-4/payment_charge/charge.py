import random
import os
import string

class PaymentAuthException(Exception):
    def __init__(self, message, info):
        super().__init__(message)
        self.message = message or 'Payment authorisation failed'
        self.details = info or {}


class PaymentChargeException(Exception):
    def __init__(self, message=None, info=None):
        super().__init__(message)

        self.message = message or "Payment charge failed"
        self.details = info or {}


def is_charge_request_valid(charge):
    return all(x in charge for x in ["customerId", "fareId", "fareAmount"])


def lambda_handler(event, context):
    if not is_charge_request_valid(event):
        raise ValueError('Invalid charge request')

    if event['customerId'].endswith('fail_auth'):
        raise PaymentAuthException('Forced auth transaction failure', event)

    if event['customerId'].endswith('fail_charge'):
        raise PaymentChargeException('Forced charge transaction failure', event)

    auth_code = provider_auth(event['fareAmount'], event['cc'], event['expiryDate'], event['cvv'])

    transaction_id = provider_charge(auth_code, event['fareAmount'])

    charge_response = {
        "customerId": event['customerId'],
        "fareId": event['fareId'],
        "fareAmount": event['fareAmount'],
        "chargeToken": auth_code,
        "chargeId": transaction_id
    }

    return charge_response


def provider_auth(amount, cc, exp, cvv):
    rand_id = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    return "tok_{0}".format(rand_id)


def provider_charge(auth_code, amount):
    rand_id = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    return "ch_{0}".format(rand_id)
