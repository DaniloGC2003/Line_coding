import tkinter as tk

BACKGROUND_COLOR = "#dde"

def retrieve_mensagem():
    print(input_mensagem.get())

janela = tk.Tk()
janela.title("Codificação de linha")
janela.geometry("500x300")
janela.configure(background=BACKGROUND_COLOR)

label_input_mensagem = tk.Label(janela, text='Digite aqui a mensagem:', 
                                background=BACKGROUND_COLOR,
                                padx=5, pady=5)
label_input_mensagem.grid(column=0, row=0)
input_mensagem = tk.Entry(janela, width=40, borderwidth=2)
input_mensagem.grid(column=0, row=1, padx=5, pady=5)
button_input_mensagem = tk.Button(janela, text='Enter', command=retrieve_mensagem)
button_input_mensagem.grid(column=1, row=1, pady=5)

janela.mainloop() 

