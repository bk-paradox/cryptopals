import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()
key = b"YELLOW SUBMARINE"
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
d = cipher.decryptor()
with open('7.txt') as f:
    ct = binascii.a2b_base64(f.read())
    pt = d.update(ct) + d.finalize()
    print(pt)
