import hashlib

def hash_with_sha256(data):
    """SHA256 ile veriyi hashle."""
    hashed_data = hashlib.sha256(data.encode()).digest()
    return hashed_data