#client: envia a mensagem
import tkinter as tk
import encoding as enc
import plotting as pltn
import NRZ_level as nrzl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import messagebox
import client

#import server as srv

BACKGROUND_COLOR = "#dde"
ENCODING = 'cp860'
CHAVE = 76

numericValuesString = []
stringCriptografada = ''
stringCriptografadaValues = []
stringBinariaMsgCriptografada = ''
msgCodificacaoLinha = []
figure_grafico = None

stringBinaria_tensoesParaBits = ''
BitsParaListaInts = []
listaInts_decriptografados = []



def retrieve_mensagem():
    mensagem = input_mensagem.get()
    print('mensagem original: ' + input_mensagem.get())
    numericValuesString = enc.getNumericValue(mensagem)
    print(numericValuesString)
    stringCriptografadaValues = enc.criptografar(numericValuesString, CHAVE)
    print(stringCriptografadaValues)
    stringCriptografada = enc.bytes_to_string(stringCriptografadaValues)
    print(stringCriptografada)

    display_mensagem_criptografada.config(text=stringCriptografada)

    #mostrar bits de msg cripografada 
    stringBinariaMsgCriptografada = enc.get_bits(stringCriptografadaValues)
    print(stringBinariaMsgCriptografada)

    #usar codificacao de linha
    msgCodificacaoLinha = nrzl.NRZ_L_encode(stringBinariaMsgCriptografada)
    print(msgCodificacaoLinha)
    print('comprimento da msg codificada: ' + str(len(msgCodificacaoLinha)))

    #pegar tensoes, transforma em bits
    stringBinaria_tensoesParaBits = nrzl.NRZ_L_decode(msgCodificacaoLinha)
    print('de tensoes para bits: ' + stringBinaria_tensoesParaBits)

    #pega bits, transforma em ints:
    print('bits pra ints: ')
    BitsParaListaInts = enc.BitStringToBytes(nrzl.NRZ_L_decode(msgCodificacaoLinha))
    print(BitsParaListaInts)

    #decriptografa lista de ints:
    listaInts_decriptografados = enc.decriptografar(BitsParaListaInts, CHAVE)
    print('lista de ints originais: ')
    print(listaInts_decriptografados)

    #mensagem oriignal: 
    print('mensagem original: ' + enc.bytes_to_string(listaInts_decriptografados))



    #plota grafico
    figure_grafico = pltn.plot_graph(msgCodificacaoLinha, nrzl.NRZ_L_yaxis(msgCodificacaoLinha))
    graph_frame = tk.Frame(frame_grafico, background=BACKGROUND_COLOR)
    graph_frame.grid(column=0, row=5)
    canvas = FigureCanvasTkAgg(figure_grafico, graph_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=6, padx=5, pady=5)

    #enviar mensagem ao servidor
    '''client.input_IP()
    client.send(stringBinaria_tensoesParaBits, client.connect_socket())
    input()
    client.send(client.DISCONNECT_MESSAGE, client.connect_socket())'''


janela = tk.Tk()
janela.title("Codificação de linha")
#janela.geometry("700x700")
janela.configure(background=BACKGROUND_COLOR)

frame_input = tk.Frame(janela, background=BACKGROUND_COLOR)
frame_input.grid(row=0, column=0)
label_input_mensagem = tk.Label(frame_input, text='Mensagem original:', 
                                background=BACKGROUND_COLOR,
                                padx=5, pady=5)
label_input_mensagem.grid(column=0, row=0)
input_mensagem = tk.Entry(frame_input, width=40, borderwidth=2)
input_mensagem.grid(column=0, row=1, padx=5, pady=5)
button_input_mensagem = tk.Button(frame_input, text='Enter', command=retrieve_mensagem)
button_input_mensagem.grid(column=1, row=1, pady=5)

frame_mensagem_criptografada = tk.Frame(janela, background=BACKGROUND_COLOR)
frame_mensagem_criptografada.grid(row=1, column=0)
label_mensagem_criptografada = tk.Label(frame_mensagem_criptografada, text='Mensagem criptografada:', 
                                background=BACKGROUND_COLOR,
                                padx=5, pady=5)
label_mensagem_criptografada.grid(column=0, row=0)
display_mensagem_criptografada = tk.Label(frame_mensagem_criptografada, background=BACKGROUND_COLOR,
                                padx=5, pady=5)
display_mensagem_criptografada.grid(column=0, row=1)

frame_grafico = tk.Frame(janela, background=BACKGROUND_COLOR)
frame_grafico.grid(row=2, column=0)



def on_closing():
    if messagebox.askokcancel("Quit", "Você quer sair?"):
        janela.quit()
        janela.destroy()


janela.protocol("WM_DELETE_WINDOW", on_closing)
janela.mainloop() 
print('oi')
plt.close()
