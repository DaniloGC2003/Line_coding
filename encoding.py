
ENCODING = 'cp860'

def getNumericValue(msg):#retorna lista com valores dos caracteres da string de acordo com o ENCODING
    valores = []
    for i in range(0, len(msg)):
        valores.append(ord(msg[i].encode(ENCODING)))
    return valores

def criptografar(bytes, key):#retorna lista de valores numericos criptografados
    bytes_criptogrfados = []
    for byte in bytes:
        new_byte = (byte + key) % 256
        bytes_criptogrfados.append(new_byte)
    return bytes_criptogrfados

def decriptografar(bytes, key):
    bytes_decriptografados = []
    for byte in bytes:
        new_byte = (byte - key) % 256
        bytes_decriptografados.append(new_byte)
    return bytes_decriptografados

x = getNumericValue('áéêê')
print(x)
print(bytes(x).decode(ENCODING))

y = criptografar(x, 400)
print(y)
print(bytes(y).decode(ENCODING))

z = decriptografar(y, 400)
print(z)
