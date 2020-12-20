import hashlib

def hash(message):
    return hashlib.sha256(message).hexdigest()

def hash_512(message):
    return hashlib.sha512(message).hexdigest()


message= b"I"
print(hash(message))
print(hash_512(message))

