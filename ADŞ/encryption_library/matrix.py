import numpy as np
import base64

def generate_matrix(rows=9, cols=9, min_val=1, max_val=10):
    
    matrix = np.random.randint(min_val, max_val + 1, size=(rows, cols))
    return matrix
    

def to_bytes(matrix):
    matrix_bytes = matrix.tobytes()
    matrix_bytes = ' '.join(format(byte, '08b') for byte in matrix_bytes)
    return matrix_bytes

   
def encoded_matrix(matrix):

    flat_matrix = matrix.flatten()

    matrix_str = ','.join(map(str, flat_matrix))
    encoded_matrix = base64.b64encode(matrix_str.encode('utf-8')).decode('utf-8')
    return encoded_matrix 
    
   

    
