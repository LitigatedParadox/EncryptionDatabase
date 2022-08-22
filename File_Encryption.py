from attr import has
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

UserGenPassword = input("Please enter a password: ")
password = UserGenPassword.encode()

mysalt = b'\xf4\x86\xed=s\xae\xa9\x7fTg>\xbc\x85\xc8\xe9\xd9'

kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256,
    length = 32,
    salt = mysalt,
    iterations = 100000,
    backend=default_backend
)

key = base64.urlsafe_b64decode(kdf.derive(password))

print(key.decode())