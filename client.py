import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = "192.168.1.118"  # socket.gethostbyname(socket.gethostname())
server_address = ''#input('server IP address: ')
addr = None#(server_address, PORT)

def input_IP():
    global server_address
    global addr
    server_address = input('server IP address: ')
    addr = (server_address, PORT)

def connect_socket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)

    return client

def send(msg, socket):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    socket.send(send_length)
    socket.send(message)
    print(socket.recv(2048).decode(FORMAT))

'''input_IP()
send("Fala tu toperá", connect_socket())
input()
send(DISCONNECT_MESSAGE, connect_socket())'''
