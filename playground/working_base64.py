import base64

encoded = base64.b64encode(b'hello2')
print(encoded)

decoded = base64.b64decode(encoded)