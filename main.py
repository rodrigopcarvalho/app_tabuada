from tkinter import *



def tabuada():
    n = int(valor.get())
    resultado_0['text'] = '{} x {:2} = {}'.format(n, 0, n * 0)
    resultado_1['text'] = '{} x {:2} = {}'.format(n, 1, n * 1)
    resultado_2['text'] = '{} x {:2} = {}'.format(n, 2, n * 2)
    resultado_3['text'] = '{} x {:2} = {}'.format(n, 3, n * 3)
    resultado_4['text'] = '{} x {:2} = {}'.format(n, 4, n * 4)
    resultado_5['text'] = '{} x {:2} = {}'.format(n, 5, n * 5)
    resultado_6['text'] = '{} x {:2} = {}'.format(n, 6, n * 6)
    resultado_7['text'] = '{} x {:2} = {}'.format(n, 7, n * 7)
    resultado_8['text'] = '{} x {:2} = {}'.format(n, 8, n * 8)
    resultado_9['text'] = '{} x {:2} = {}'.format(n, 9, n * 9)
    resultado_10['text'] ='{} x {:2} = {}'.format(n, 10, n * 10)



#Cores
ciano = '#00CED1'
snow = '#FFFAFA'
black = '#000000'

janela = Tk()
janela.title('Version 1.0.0')
janela.geometry('295x525+500+80')
janela.resizable(width=False, height=True)
janela.configure(bg=snow)

#width = largura
#height = altura


# DIVIDINDO A JANELA EM DUAS PARTES
quadro_cima = Frame(janela, width=295, height=50, bg=snow, pady=0, padx=0, relief='flat', )
quadro_cima.grid(row=0, column=0, sticky=NSEW)

quadro_baixo = Frame(janela,width=290, height=180, bg=snow, pady=0, padx=0, relief='flat', )
quadro_baixo.grid(row=1, column=0, sticky=NSEW)

# QUADRO DE CIMA
titulo = Label(quadro_cima, text='MINHA TABUADA',
               width=23,
               height=2,
               padx=0,
               relief='flat',
               anchor='center',
               font='Ivy 16 bold',
               bg=snow,
               fg=black)
titulo.place(x=0, y=0)


linha = Label(quadro_cima,
              text='',
              width=400,
              height=2,
              padx=0,
              relief='flat',
              anchor='center',
              font='Ivy 1',
              bg=ciano,
              fg=ciano)
linha.place(x=0, y=45)

# QUADRO DE BAIXO
texto_orientacao = Label(quadro_baixo,
                         text='DIGITE A TABUADA DESEJADA',
                         width=23,
                         height=1,
                         padx=20,
                         relief='flat',
                         anchor='center',
                         font='Ivy 12 bold',
                         bg=snow,
                         fg=black)
texto_orientacao.grid(row=0, column=0, sticky=NSEW, pady=10, padx=10)


valor = Entry(quadro_baixo,
               relief='solid',
               justify='center',
               border=3,
               font='Ivy 10 bold',)
valor.grid(row=1, column=0, sticky=NSEW, pady=0, padx=50)


botao = Button(quadro_baixo,
               text='CLIQUE AQUI',
               command=tabuada,
               width=10,
               height=2,
               border=1,
               relief='sunken',
               anchor='center',
               font='Ivy 10 bold',
               bg=ciano,
               fg=black)
botao.grid(row=2, column=0, sticky=NSEW, pady=10, padx=5, columnspan=3)


resultado_0 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_0.grid(row=3, column=0, sticky=NSEW, pady=1, padx=5)

resultado_1 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_1.grid(row=4, column=0, sticky=NSEW, pady=1, padx=5)

resultado_2 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_2.grid(row=5, column=0, sticky=NSEW, pady=1, padx=5)

resultado_3 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_3.grid(row=6, column=0, sticky=NSEW, pady=1, padx=5)

resultado_4 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_4.grid(row=7, column=0, sticky=NSEW, pady=1, padx=5)

resultado_5 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_5.grid(row=8, column=0, sticky=NSEW, pady=1, padx=5)

resultado_6 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_6.grid(row=9, column=0, sticky=NSEW, pady=1, padx=5)

resultado_7 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_7.grid(row=10, column=0, sticky=NSEW, pady=1, padx=5)

resultado_8 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_8.grid(row=11, column=0, sticky=NSEW, pady=1, padx=5)

resultado_9 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_9.grid(row=12, column=0, sticky=NSEW, pady=1, padx=5)

resultado_10 = Label(quadro_baixo,
               text='--------',
               width=2,
               height=1,
               border=3,
               relief='solid',
               font='Ivy 11 bold',
               bg=ciano,
               fg=black)
resultado_10.grid(row=13, column=0, sticky=NSEW, pady=1, padx=5)


rodape = Label(quadro_baixo,
               text='Desenvolvido por: Rodrigo Carvalho',
               width=23,
               height=2,
               relief='flat',
               anchor='center',
               font='Ivy 7 bold',
               bg=snow,
               fg=black)
rodape.grid(row=15, column=0, sticky=NSEW)




janela.mainloop()