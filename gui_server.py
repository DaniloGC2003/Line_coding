import tkinter as tk
import encoding as enc
import plotting as pltn
import NRZ_level as nrzl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import messagebox

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
    graph_frame = tk.Frame(janela)
    graph_frame.grid(column=0, row=5)
    canvas = FigureCanvasTkAgg(figure_grafico, graph_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=6)


janela = tk.Tk()
janela.title("Codificação de linha")
#janela.geometry("500x300")
janela.configure(background=BACKGROUND_COLOR)

label_input_mensagem = tk.Label(janela, text='Mensagem original:', 
                                background=BACKGROUND_COLOR,
                                padx=5, pady=5)
label_input_mensagem.grid(column=0, row=0)
input_mensagem = tk.Entry(janela, width=40, borderwidth=2)
input_mensagem.grid(column=0, row=1, padx=5, pady=5)
button_input_mensagem = tk.Button(janela, text='Enter', command=retrieve_mensagem)
button_input_mensagem.grid(column=1, row=1, pady=5)

label_mensagem_criptografada = tk.Label(janela, text='Mensagem criptografada:', 
                                background=BACKGROUND_COLOR,
                                padx=5, pady=5)
label_mensagem_criptografada.grid(column=0, row=3)
display_mensagem_criptografada = tk.Label(janela, background=BACKGROUND_COLOR,
                                padx=5, pady=5)
display_mensagem_criptografada.grid(column=0, row=4)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        janela.quit()
        janela.destroy()


janela.protocol("WM_DELETE_WINDOW", on_closing)
janela.mainloop() 
print('oi')
plt.close()

