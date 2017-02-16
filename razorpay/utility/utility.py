import hmac
import hashlib


class Utility(object):
    def __init__(self, client=None):
        self.client = client

    def verify_payment_signature(self, parameters):
        order_id = parameters['order_id']
        payment_id = parameters['payment_id']
        razorpay_signature = parameters['razorpay_signature']
        msg = "{}|{}".format(order_id, payment_id)
        dig = hmac.new(key=self.client.auth[1],
                       msg=msg,
                       digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        if not hmac.compare_digest(generated_signature, razorpay_signature):
            raise ValueError('Payment Signature Verification Failed')

        return True
