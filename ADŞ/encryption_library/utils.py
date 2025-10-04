import base64

def encode_bs64(data):
    """To base64"""
    return base64.b64encode(data).decode('utf-8')

def decode_bs64(data):
    """get base64"""
    return base64.b64decode(data.encode('utf-8'))
