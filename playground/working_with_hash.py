import hashlib


data = "1glk;jhjifgjhgoujfjihgiufgihufgoiuhifg1їїї".encode()
print(data)

hash_value = hashlib.sha256(data).hexdigest()
print(hash_value)


hash_value = hashlib.md5(data).hexdigest()

data = "Hello".encode()
print(data)

hash_value = hashlib.sha256(data).hexdigest()

print(hash_value)