# # from cryptography.fernet import Fernet
# # print(Fernet.generate_key().decode())
# import base64

# key = "key"
# decoded_key = base64.urlsafe_b64decode(key)
# print(len(decoded_key))  # This will give you the length in bytes
import os
import base64

key = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
print(key)
