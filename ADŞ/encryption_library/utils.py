import base64

def encode_bs64(data):
    """Veriyi Base64 formatına kodla."""
    return base64.b64encode(data).decode('utf-8')

def decode_bs64(data):
    """Base64 fomatındaki veriyi çöz."""
    return base64.b64decode(data.encode('utf-8'))