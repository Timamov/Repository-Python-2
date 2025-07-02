import datetime
import jwt
import time
secret = 'soihcdwjefve'

payload = {
    'my_name': 'Timur',
    'age': 13,
    'favourite_city': 'Vienna',
    'iat': datetime.datetime.now() + datetime.timedelta(seconds=500)

}
time.sleep(12)

encode_jwt = jwt.encode(
    payload=payload,
    key=secret,
    algorithm='HS256'
)
print(encode_jwt)

decoded = jwt.decode(
    encode_jwt,
    '1234',
    algorithms=['HS256']
)
print(decoded)