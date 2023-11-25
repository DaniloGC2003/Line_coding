# client: envia a mensagem
import tkinter as tk
import encoding as enc
import plotting as pltn
import NRZ_level as nrzl
import NRZ_invert as nrzi
import RZ as rz
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
from tkinter import messagebox
import client
import numpy as np

BACKGROUND_COLOR = "#dde"
ENCODING = 'cp860'
CHAVE = 76

mensagem_original = ''
numericValuesString = []
stringCriptografada = ''
stringCriptografadaValues = []
stringBinariaMsgCriptografada = ''
msgCodificacaoLinha = []
figure_grafico = None

stringBinaria_tensoesParaBits = ''
BitsParaListaInts = []
listaInts_decriptografados = []


def executar_NRZL(mensagem):
    global numericValuesString
    global stringCriptografada
    global stringCriptografadaValues
    global stringBinariaMsgCriptografada
    global msgCodificacaoLinha
    global figure_grafico
    global stringBinaria_tensoesParaBits
    global BitsParaListaInts
    global listaInts_decriptografados

    numericValuesString = enc.getNumericValue(mensagem)
    #print(numericValuesString)
    stringCriptografadaValues = enc.criptografar(numericValuesString, CHAVE)
    #print(stringCriptografadaValues)
    stringCriptografada = enc.bytes_to_string(stringCriptografadaValues)
    #print(stringCriptografada)

    

    # mostrar bits de msg cripografada
    stringBinariaMsgCriptografada = enc.get_bits(stringCriptografadaValues)
    #print(stringBinariaMsgCriptografada)

    # usar codificacao de linha
    msgCodificacaoLinha = nrzl.NRZ_L_encode(stringBinariaMsgCriptografada)
    #print(msgCodificacaoLinha)
    #print('comprimento da msg codificada: ' + str(len(msgCodificacaoLinha)))

    # pegar tensoes, transforma em bits
    stringBinaria_tensoesParaBits = nrzl.NRZ_L_decode(msgCodificacaoLinha)
    #print('de tensoes para bits: ' + stringBinaria_tensoesParaBits)

    # pega bits, transforma em ints:
    #print('bits pra ints: ')
    BitsParaListaInts = enc.BitStringToBytes(stringBinaria_tensoesParaBits)
    #print(BitsParaListaInts)

    # decriptografa lista de ints:
    listaInts_decriptografados = enc.decriptografar(BitsParaListaInts, CHAVE)
    #print('lista de ints originais: ')
    #print(listaInts_decriptografados)

    # mensagem oriignal:
    #print('mensagem original: ' + enc.bytes_to_string(listaInts_decriptografados))


    # plota grafico
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    figure_grafico = pltn.plot_graph(
        msgCodificacaoLinha, nrzl.NRZ_L_yaxis(msgCodificacaoLinha))
    # graph_frame = tk.Frame(frame_grafico, background=BACKGROUND_COLOR)
    # graph_frame.grid(column=0, row=5)
    canvas = FigureCanvasTkAgg(figure_grafico, frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=6, padx=5, pady=5)

def executar_RZ(mensagem):
    global numericValuesString
    global stringCriptografada
    global stringCriptografadaValues
    global stringBinariaMsgCriptografada
    global msgCodificacaoLinha
    global figure_grafico
    global stringBinaria_tensoesParaBits
    global BitsParaListaInts
    global listaInts_decriptografados

    numericValuesString = enc.getNumericValue(mensagem)
    #print(numericValuesString)
    stringCriptografadaValues = enc.criptografar(numericValuesString, CHAVE)
    #print(stringCriptografadaValues)
    stringCriptografada = enc.bytes_to_string(stringCriptografadaValues)
    #print(stringCriptografada)

    # colocar msg criptografada na tela
    display_mensagem_criptografada.config(text=stringCriptografada)

    # mostrar bits de msg cripografada
    stringBinariaMsgCriptografada = enc.get_bits(stringCriptografadaValues)
    #print(stringBinariaMsgCriptografada)

    # usar codificacao de linha
    msgCodificacaoLinha = rz.RZ_encode(stringBinariaMsgCriptografada)
    #print(msgCodificacaoLinha)
    #print('comprimento da msg codificada: ' + str(len(msgCodificacaoLinha)))

    # pegar tensoes, transforma em bits
    stringBinaria_tensoesParaBits = rz.RZ_decode(msgCodificacaoLinha)
    #print('de tensoes para bits: ' + stringBinaria_tensoesParaBits)

    # pega bits, transforma em ints:
    #print('bits pra ints: ')
    BitsParaListaInts = enc.BitStringToBytes(stringBinaria_tensoesParaBits)
    #print(BitsParaListaInts)

    # decriptografa lista de ints:
    listaInts_decriptografados = enc.decriptografar(BitsParaListaInts, CHAVE)
    #print('lista de ints originais: ')
    #print(listaInts_decriptografados)

    # mensagem oriignal:
    #print('mensagem original: ' + enc.bytes_to_string(listaInts_decriptografados))

    # plota grafico
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    figure_grafico = pltn.plot_graph(
        msgCodificacaoLinha, rz.RZ_yaxis(msgCodificacaoLinha))
    # graph_frame = tk.Frame(frame_grafico, background=BACKGROUND_COLOR)
    # graph_frame.grid(column=0, row=5)
    canvas = FigureCanvasTkAgg(figure_grafico, frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=6, padx=5, pady=5)

def executar_NRZ_I(mensagem):
    global numericValuesString
    global stringCriptografada
    global stringCriptografadaValues
    global stringBinariaMsgCriptografada
    global msgCodificacaoLinha
    global figure_grafico
    global stringBinaria_tensoesParaBits
    global BitsParaListaInts
    global listaInts_decriptografados

    numericValuesString = enc.getNumericValue(mensagem)
    #print(numericValuesString)
    stringCriptografadaValues = enc.criptografar(numericValuesString, CHAVE)
    #print(stringCriptografadaValues)
    stringCriptografada = enc.bytes_to_string(stringCriptografadaValues)
    #print(stringCriptografada)

    # colocar msg criptografada na tela
    display_mensagem_criptografada.config(text=stringCriptografada)

    # mostrar bits de msg cripografada
    stringBinariaMsgCriptografada = enc.get_bits(stringCriptografadaValues)
    #print(stringBinariaMsgCriptografada)

    # usar codificacao de linha
    msgCodificacaoLinha = nrzi.NRZ_I_encode(stringBinariaMsgCriptografada)
    #print(msgCodificacaoLinha)
    #print('comprimento da msg codificada: ' + str(len(msgCodificacaoLinha)))

    # pegar tensoes, transforma em bits
    stringBinaria_tensoesParaBits = nrzi.NRZ_I_decode(msgCodificacaoLinha)
    #print('de tensoes para bits: ' + stringBinaria_tensoesParaBits)

    # pega bits, transforma em ints:
    #print('bits pra ints: ')
    BitsParaListaInts = enc.BitStringToBytes(stringBinaria_tensoesParaBits)
    #print(BitsParaListaInts)

    # decriptografa lista de ints:
    listaInts_decriptografados = enc.decriptografar(BitsParaListaInts, CHAVE)
    #print('lista de ints originais: ')
    #print(listaInts_decriptografados)

    # mensagem oriignal:
    #print('mensagem original: ' + enc.bytes_to_string(listaInts_decriptografados))

    # plota grafico
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    figure_grafico = pltn.plot_graph(
        msgCodificacaoLinha, nrzi.NRZ_I_yaxis(msgCodificacaoLinha))
    # graph_frame = tk.Frame(frame_grafico, background=BACKGROUND_COLOR)
    # graph_frame.grid(column=0, row=5)
    canvas = FigureCanvasTkAgg(figure_grafico, frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=6, padx=5, pady=5)

def retrieve_mensagem():
    mensagem = input_mensagem.get()
    mensagem_original = mensagem
    #print('mensagem original: ' + input_mensagem.get())

    if codificacao.get() == 'NRZ-L':
        executar_NRZL(mensagem_original)
    elif codificacao.get() == 'RZ':
        executar_RZ(mensagem_original)
    elif codificacao.get() == 'NRZ-I':
        executar_NRZ_I(mensagem_original)

    # colocar msg criptografada na tela
    display_mensagem_criptografada.config(text=stringCriptografada)
    display_mensagem_binario.config(text=stringBinariaMsgCriptografada)

def setServerData():
    client.server_address = input_IP.get()
    client.addr = (client.server_address, client.PORT)

    client.send(str(msgCodificacaoLinha), client.connect_socket())


janela = tk.Tk()
janela.title("Codificação de linha - cliente")
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
button_input_mensagem.grid(column=1, row=1, pady=5, padx=(5, 10))


label_IP = tk.Label(frame_input, text='Endereço IP do servidor: ', background=BACKGROUND_COLOR)
label_IP.grid(row=0, column=2)
input_IP = tk.Entry(frame_input, width=40, borderwidth=2)
input_IP.grid(column=2, row=1, padx=(10, 5), pady=5)
button_input_IP = tk.Button(frame_input, text='Enter', command=setServerData)
button_input_IP.grid(column=3, row=1, padx=5)


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
label_mensagem_binario = tk.Label(frame_mensagem_criptografada, text='Mensagem em binário:', background=BACKGROUND_COLOR, padx=5, pady=5)
label_mensagem_binario.grid(row=2, column=0)
display_mensagem_binario = tk.Label(frame_mensagem_criptografada, background=BACKGROUND_COLOR, padx=5, pady=5)
display_mensagem_binario.grid(row=3, column=0)

frame_grafico = tk.Frame(janela, background=BACKGROUND_COLOR)
frame_grafico.grid(row=3, column=0)


def on_closing():
    if messagebox.askokcancel("Quit", "Você quer sair?"):
        janela.quit()
        janela.destroy()


janela.protocol("WM_DELETE_WINDOW", on_closing)
janela.mainloop()
plt.close()
