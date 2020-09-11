"""
    JWT
"""

import base64
import json
import hmac


class JWT:
    def __init__(self):
        pass

    @staticmethod
    def encode(key):
        # header
        json_header = {
            'alg': 'HS256',
            'typ': 'JWT'
        }
        base64_header = base64.b64encode(json.dumps(json_header).encode())

        # payload
        json_payload = {
            'exp': 300,
        }
        base64_payload = base64.b64encode(json.dumps(json_payload).encode())

        # sign

        b64_ = base64_header + '.' + base64_payload
        str_hmac = hmac.new(key.encode(), b64_, digetmod='SHA256').hexdigest()
        base64_sign = base64.b64encode(json.dumps(str_hmac).encode())

        return base64_header + '.' + base64_payload + '.' + base64_sign
