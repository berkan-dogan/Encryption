import hashlib
import os

def generate_key(password, salt=None, iterations=100000, key_length=32):
    """PBKDF2 kullanarak anahtar türet."""
    if salt is None:
        salt = os.urandom(32)  # Varsayılan olarak 32 baytlık salt
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen=key_length)
    return key, salt