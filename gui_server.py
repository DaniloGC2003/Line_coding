import tkinter as tk
import encoding as enc
import plotting as pltn
import NRZ_level as nrzl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import messagebox
import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

BACKGROUND_COLOR = "#dde"
ENCODING = 'cp860'
CHAVE = 76

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

window_open = False
running = True

mensagem_recebida = ''
mensagem_recebida_list = []
numericValuesString = []
stringCriptografada = ''
stringCriptografadaValues = []
stringBinariaMsgCriptografada = ''
msgCodificacaoLinha = []
figure_grafico = None

stringBinaria_tensoesParaBits = ''
BitsParaListaInts = []
listaInts_decriptografados = []

def handle_client(conn, addr):
    global mensagem_recebida
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg ==  DISCONNECT_MESSAGE:
                connected = False
            else:
                mensagem_recebida = msg

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
    print('msg recebida: ')
    print(mensagem_recebida)
    open_window()


def start():
    server.listen()
    print(f"[LISTENING] Server is Listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    



def open_window():
    def executar_NRZI(frame):
        pass

    def executar_NRZL(frame):
        print('printa grafico')
        for widget in frame.winfo_children():
            widget.destroy()
        figure_grafico = pltn.plot_graph(
            mensagem_recebida_list, nrzl.NRZ_L_yaxis(mensagem_recebida_list))
        canvas = FigureCanvasTkAgg(figure_grafico, frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=6, padx=5, pady=5)
        

    def executar_RZ(frame):
        pass

    def retrieve_mensagem():
        global mensagem_recebida_list
        #transforma string de volta em lista
        mensagem_recebida_list = eval(mensagem_recebida)
        print(mensagem_recebida_list)
        print(type(mensagem_recebida_list))
        print('retireive')
        print(codificacao.get())

        if codificacao.get() == 'NRZ-I':
            executar_NRZI(frame_grafico)
        elif codificacao.get() == 'NRZ-L':
            executar_NRZL(frame_grafico)
        elif codificacao.get() == 'RZ':
            executar_RZ(frame_grafico)

    global window_open
    window_open = True

    janela = tk.Tk()
    janela.title("Codificação de linha")
    # janela.geometry("700x700")
    janela.configure(background=BACKGROUND_COLOR)

    frame_input = tk.Frame(janela, background=BACKGROUND_COLOR)
    frame_input.grid(row=0, column=0)
    label_input_mensagem = tk.Label(frame_input, text='Mensagem original:',
                                    background=BACKGROUND_COLOR,
                                    padx=5, pady=5)
    label_input_mensagem.grid(column=0, row=0)
    input_mensagem = tk.Entry(frame_input, width=40, borderwidth=2)
    input_mensagem.grid(column=0, row=1, padx=5, pady=5)
    button_input_mensagem = tk.Button(
        frame_input, text='Enter', command=retrieve_mensagem)
    button_input_mensagem.grid(column=1, row=1, pady=5)

    frame_codificacao = tk.Frame(janela, background=BACKGROUND_COLOR)
    frame_codificacao.grid(row=1, column=0)
    label_codificacao = tk.Label(
        frame_codificacao, text='algoritmo de codificação de linha a ser usado: ', background=BACKGROUND_COLOR)
    label_codificacao.grid(column=0, row=0)
    codificacao = tk.StringVar()
    codificacao.set('NRZ-L')
    dropMenu = tk.OptionMenu(frame_codificacao, codificacao, 'NRZ-L', 'RZ', 'NRZ-I')
    dropMenu.grid(column=1, row=0)

    frame_mensagem_criptografada = tk.Frame(janela, background=BACKGROUND_COLOR)
    frame_mensagem_criptografada.grid(row=2, column=0)
    label_mensagem_criptografada = tk.Label(frame_mensagem_criptografada, text='Mensagem criptografada:',
                                            background=BACKGROUND_COLOR,
                                            padx=5, pady=5)
    label_mensagem_criptografada.grid(column=0, row=0)
    display_mensagem_criptografada = tk.Label(frame_mensagem_criptografada, background=BACKGROUND_COLOR,
                                            padx=5, pady=5)
    display_mensagem_criptografada.grid(column=0, row=1)

    frame_grafico = tk.Frame(janela, background=BACKGROUND_COLOR)
    frame_grafico.grid(row=3, column=0)

    janela.mainloop()

    window_open = False

start()