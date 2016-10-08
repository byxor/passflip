import hashlib


def mutate(password, salt):
    combined = password + salt
    return hashlib.sha224(combined.encode("utf-8")).hexdigest()

