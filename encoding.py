from textwrap import wrap

ENCODING = 'cp860'

def getNumericValue(msg):#retorna lista com valores dos caracteres da string de acordo com o ENCODING
    valores = []
    for i in range(0, len(msg)):
        valores.append(ord(msg[i].encode(ENCODING)))
    return valores

def criptografar(bytes, key):#retorna lista de valores numericos criptografados
    bytes_criptogrfados = []
    for byte in bytes:
        # operacao bit a bit seguida de deslocamento
        new_byte = ((byte ^ key) + key) % 256
        bytes_criptogrfados.append(new_byte)
    return bytes_criptogrfados

def decriptografar(bytes, key):
    bytes_decriptografados = []
    for byte in bytes:
        new_byte = (byte - key) % 256
        new_byte = (new_byte ^ key)
        bytes_decriptografados.append(new_byte)
    return bytes_decriptografados

def get_bits(bytes):#recebe lista com inteiros. retorna string de bits    FIX
    msg_in_bits = ''
    for byte in bytes:
        msg_in_bits += int_to_binString(byte)
    return msg_in_bits

def int_to_binString(num):#recebe int, retorna string de bits
    bin_num = str(bin(num))
    bin_string = ''
    for i in range(2, len(bin_num)):
        bin_string += bin_num[i]
    while len(bin_string) != 8:
        bin_string = '0' + bin_string
    return bin_string

def bytes_to_string(byte_list):
    return bytes(byte_list).decode(ENCODING)

def BitStringToBytes(bit_string):#recebe string de bits, retorna lista com valores inteiros
    bytes = []
    separated_bits = wrap(bit_string, 8)

    for bits in separated_bits:
        bytes.append(int(bits, 2))
    
    return bytes




'''
x = getNumericValue('áéêê')
print(x)
print(bytes(x).decode(ENCODING))

y = criptografar(x, 400)
print(y)
print(bytes(y).decode(ENCODING))

z = decriptografar(y, 400)
print(z)
'''

