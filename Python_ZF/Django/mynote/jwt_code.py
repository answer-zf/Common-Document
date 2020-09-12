"""
    JWT
"""

import base64
import json
import hmac
import copy
import time


class JWT:

    @staticmethod
    def encode(payload, key, exp=300):
        """
            JWT 加密
        :param payload: 自定义 json
        :param key: 密钥  str / bytes
        :param exp: 超时失效时间 时间戳 int
        :return: token bytes
        """
        json_header = {
            'alg': 'HS256',
            'typ': 'JWT'
        }
        # separators 第一个参数：json串中 键值对以 xx 连接符相连
        #           第二个参数：键值 以 xx 连接符相连
        #          作用是去掉'，' '：'后面的空格，在传输数据的过程中，越精简越好，冗余的东西全部去掉。
        # sort_keys 作用：告诉编码器按照字典key排序(a到z)输出
        str_json_header = json.dumps(
            json_header, separators=(',', ':'), sort_keys=True)  # json 串 紧凑有序
        byte_base64_header = JWT.b64encode(str_json_header.encode())

        # payload
        json_payload = copy.deepcopy(payload)
        json_payload['exp'] = int(time.time() + exp)
        str_json_payload = json.dumps(
            json_payload, separators=(',', ':'), sort_keys=True)
        byte_base64_payload = JWT.b64encode(
            str_json_payload.encode())

        # sign
        b64_ = byte_base64_header + b'.' + byte_base64_payload

        if isinstance(key, str):
            key = key.encode()
        byte_hmac = hmac.new(key, b64_, digestmod='SHA256').digest()
        byte_base64_sign = JWT.b64encode(byte_hmac)

        return byte_base64_header + b'.' + byte_base64_payload + b'.' + byte_base64_sign

    @staticmethod
    def decode(token, key):
        """
            校验 token
        :param token: 加密后的 token bytes
        :param key: 密钥 str / bytes
        :return: 成功 payload json ,失败 抛出异常
        """

        header_bs, payload_bs, sign = token.split(b'.')

        if isinstance(key, str):
            key = key.encode()

        byte_hmac = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256').digest()
        now_sign = JWT.b64encode(byte_hmac)

        if sign != now_sign:
            raise JWTError('Token is invalid')

        json_payload = json.loads(JWT.b64decode(payload_bs).decode())
        # 过期时间戳
        exp = json_payload['exp']
        now_time = time.time()
        if now_time > exp:
            raise JWTError('Token is expired')

        return json_payload

    @staticmethod
    def b64encode(byte_):
        """
            base64 加密后，
        :param byte_:
        :return:
        """
        # 替换原生 base64 '=' -> ''
        return base64.urlsafe_b64encode(byte_).replace(b'=', b'')

    @staticmethod
    def b64decode(byte_):
        # 还原 base64 '=',并解码
        rem = len(byte_) % 4
        byte_ += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(byte_)


class JWTError(Exception):
    """
        自定义异常
    """
    def __init__(self, error_msg):
        self.error = error_msg

    def __str__(self):
        return '<JWTError error %s>' % self.error


if __name__ == '__main__':
    JWT_byte = JWT.encode({'abc': '124', 'def': 'eee'}, 'answer')
    print(JWT.decode(JWT_byte, 'answer'))
