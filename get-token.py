#!/usr/bin/env python3
import jwt
import uuid
import datetime

api_key = '69bbc9aa-9bcd-4c60-91c9-c582024e3361'
secret_key = '02c56a651682a76c3904cb824febb6ab4a09c664f9909cecb24fe1aaee131af2'


def generateToken():
    expires = 24 * 3600
    now = datetime.datetime.utcnow()
    exp = now + datetime.timedelta(seconds=expires)
    return jwt.encode(payload={
        'apikey': api_key
        }, key=secret_key).decode('utf-8')

if __name__ == '__main__':
    print(generateToken())