import tkinter as tk
import encoding as enc
import plotting as pltn
import NRZ_level as nrzl

BACKGROUND_COLOR = "#dde"
ENCODING = 'cp860'
CHAVE = 3

numericValuesString = []
stringCriptografada = ''
stringCriptografadaValues = []
stringBinariaMsgCriptografada = ''
msgCodificacaoLinha = []

def retrieve_mensagem():
    mensagem = input_mensagem.get()
    print(input_mensagem.get())
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

    msgCodificacaoLinha = nrzl.NRZ_L_encode(stringBinariaMsgCriptografada)
    print(msgCodificacaoLinha)
    print('comprimento da msg codificada: ' + str(len(msgCodificacaoLinha)))

    #plota grafico
    pltn.plot_graph(msgCodificacaoLinha, nrzl.NRZ_L_yaxis(msgCodificacaoLinha))


janela = tk.Tk()
janela.title("Codificação de linha")
janela.geometry("500x300")
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

janela.mainloop() 

