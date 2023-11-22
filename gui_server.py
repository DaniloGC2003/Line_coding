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
                connected = False

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
        #thread = threading.Thread(target=handle_client, args=(conn, addr))
        #thread.start()
        handle_client(conn, addr)
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    



def open_window():
    def executar_NRZI(frame):
        pass

    def executar_NRZL(frame):
        global stringBinaria_tensoesParaBits
        global BitsParaListaInts
        global listaInts_decriptografados

        print('printa grafico')
        for widget in frame.winfo_children():
            widget.destroy()
        figure_grafico = pltn.plot_graph(
            mensagem_recebida_list, nrzl.NRZ_L_yaxis(mensagem_recebida_list))
        canvas = FigureCanvasTkAgg(figure_grafico, frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=6, padx=5, pady=5)

        print('msg recebida list: ', end='')
        print(mensagem_recebida_list)
        stringBinaria_tensoesParaBits = nrzl.NRZ_L_decode(mensagem_recebida_list)
        print('de tensoes para bits: ' + stringBinaria_tensoesParaBits)
        BitsParaListaInts = enc.BitStringToBytes(stringBinaria_tensoesParaBits)
        print('string to byets: ', end='')
        print(BitsParaListaInts)

        display_mensagem_criptografada.config(text=enc.bytes_to_string(BitsParaListaInts))

        listaInts_decriptografados = enc.decriptografar(BitsParaListaInts, CHAVE)
        print('lista de ints originais: ', end='')
        print(listaInts_decriptografados)

        display_mensagem_original.config(text=enc.bytes_to_string(listaInts_decriptografados))




        

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



    def on_closing():
        if messagebox.askokcancel("Quit", "Você quer sair?"):
            janela.quit()
            janela.destroy()


    global window_open
    window_open = True

    janela = tk.Tk()
    janela.title("Codificação de linha - servidor")
    janela.configure(background=BACKGROUND_COLOR)

    label_endereco_servidor = tk.Label(janela, text='IP do servidor: ' + SERVER, justify='left', background=BACKGROUND_COLOR, padx=5, pady=5)
    label_endereco_servidor.grid(row=0, column=0)

    frame_input = tk.Frame(janela, background=BACKGROUND_COLOR)
    frame_input.grid(row=2, column=0)

    frame_codificacao = tk.Frame(janela, background=BACKGROUND_COLOR, padx=5, pady=5)
    frame_codificacao.grid(row=1, column=0)

    label_codificacao = tk.Label(
        frame_codificacao, text='algoritmo de codificação de linha a ser usado: ', background=BACKGROUND_COLOR, padx=5, pady=5)
    label_codificacao.grid(column=0, row=1)
    codificacao = tk.StringVar()
    codificacao.set('NRZ-L')
    dropMenu = tk.OptionMenu(frame_codificacao, codificacao, 'NRZ-L', 'RZ', 'NRZ-I')
    dropMenu.grid(column=1, row=1)

    button_input_mensagem = tk.Button(
        frame_input, text='Enter', command=retrieve_mensagem)
    button_input_mensagem.grid(column=1, row=1, pady=5)

    frame_grafico = tk.Frame(janela, background=BACKGROUND_COLOR)
    frame_grafico.grid(row=3, column=0)

    frame_mensagens = tk.Frame(janela, background=BACKGROUND_COLOR)
    frame_mensagens.grid(row=4, column=0)
    label_mensagem_criptografada = tk.Label(frame_mensagens, text='Mensagem criptografada:',
                                            background=BACKGROUND_COLOR,
                                            padx=5, pady=5)
    label_mensagem_criptografada.grid(column=0, row=0)
    display_mensagem_criptografada = tk.Label(frame_mensagens, background=BACKGROUND_COLOR,
                                            padx=5, text='weima')
    display_mensagem_criptografada.grid(column=0, row=1)

    label_mensagem_original = tk.Label(frame_mensagens, background=BACKGROUND_COLOR, padx=5, pady=5, text='Mensagem original:')
    label_mensagem_original.grid(column=0, row=2)
    display_mensagem_original = tk.Label(frame_mensagens, background=BACKGROUND_COLOR, padx=5, text='fala tu topera')
    display_mensagem_original.grid(column=0, row=3)

    
    

    janela.protocol("WM_DELETE_WINDOW", on_closing)
    janela.mainloop()

    window_open = False

start()
open_window()