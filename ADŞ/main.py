from encryption_library.keygen import generate_key
from encryption_library.matrix import generate_matrix, encoded_matrix , to_bytes
from encryption_library.utils import encode_bs64,decode_bs64
from encryption_library.hashing import hash_with_sha256

# Veriyi byte olarak almak için bir örnek
def xor_bytes(matrix_bytes, data_bytes):
    # Eğer verinin uzunluğu matrise eşitse XOR işlemi yapılabilir
    if len(matrix_bytes) != len(data_bytes):
        raise ValueError("Matrix ve veri uzunluğu eşit olmalı.")
    return bytes([m ^ d for m, d in zip(matrix_bytes, data_bytes)])

# Anahtar ve matrix üretimi
matrix = generate_matrix()
encoded_matrix_str = encoded_matrix(matrix)

# Matrisi bytes formatına çevir
matrix_bytes = bytes(matrix.tobytes())
print("Matrix Bytes:", matrix_bytes)

# XOR işlemi yapılacak veri
data = "Bu bir test mesajıdır."  # Buradaki veriyi değiştirebilirsiniz
data_bytes = data.encode('utf-8')

# XOR işlemi uygulama
try:
    result = xor_bytes(matrix_bytes, data_bytes)
    print("XOR Sonucu:", result)
except ValueError as e:
    print(e)
