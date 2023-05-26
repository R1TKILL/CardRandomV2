from tkinter import *
from CardClass import *

import os
import random


def voltar_Login():
    information_frame.place_forget()
    game_frame.place_forget()
    victories_frame.place_forget()
    defeats_frame.place_forget()
    points_frame.place_forget()
    reset_frame.place_forget()
    loop_frame.place_forget()
    initial_frame.place(width=980, height=580)


def context_game():
    initial_frame.place_forget()
    game_frame.place_forget()
    victories_frame.place_forget()
    defeats_frame.place_forget()
    points_frame.place_forget()
    reset_frame.place_forget()
    loop_frame.place_forget()
    information_frame.place(width=980, height=580)

    lb_backgroud = Label(information_frame, image=imgBackground)
    lb_backgroud.place(x=-60, y=-50, width=1100, height=640)

    btnVoltar = Button(information_frame, width=7, height=1, text="Voltar", activebackground="yellow",
                       activeforeground="red")
    btnVoltar.configure(font=("Arial, bold", 12), highlightbackground="yellow", highlightthickness=1, bd=3,
                        foreground="yellow", background="red", command=voltar_Login)
    btnVoltar.place(x=30, y=30)

    lb_information = Label(information_frame, background="green", foreground="yellow", font=("Arial", 16),
                           text="Este jogo consiste em adivinhar a carta aleatória gerada pelo programa, tanto o valor quanto o naipe\n"
                                " sorteado, você tera 15 chances para adivinhar os valores.")
    lb_information.place(x=10, y=110)

    lb_information2 = Label(information_frame, background="green", foreground="yellow", font=("Arial", 18),
                            text="Os valores existentes são [As,2,3,4,5,6,7,8,9,J,Q,K]")
    lb_information2.place(x=200, y=190)

    lb_information3 = Label(information_frame, background="green", foreground="yellow", font=("Arial", 18),
                            text="E os naipes são [Paus,Ouros,Copas,Espadas]")
    lb_information3.place(x=230, y=250)

    lb_information4 = Label(information_frame, background="green", foreground="yellow", font=("Arial", 20),
                            text="<<<Boa Sorte!!!>>>")
    lb_information4.place(x=350, y=330)

    btnConfirm = Button(information_frame, width=8, height=1, text="Entendi", activebackground="yellow",
                        activeforeground="red")
    btnConfirm.configure(font=("Arial, bold", 18), highlightbackground="yellow", highlightthickness=1, bd=3,
                         foreground="yellow", background="red", command=init)
    btnConfirm.place(x=390, y=430)


def init():
    position = random.randint(0, 51)
    value_random = [cards[position].get_value(), cards[position].get_suit()]
    imgCard_sorted = PhotoImage(file=getImages + "/images/" + str(value_random[0]) + "_" + str(value_random[1]) + "_.png")
    print(value_random)#Teste

    def Game(ls):
        initial_frame.place_forget()
        information_frame.place_forget()
        victories_frame.place_forget()
        defeats_frame.place_forget()
        points_frame.place_forget()
        reset_frame.place_forget()
        loop_frame.place_forget()
        game_frame.place(width=980, height=580)

        lb_backgroud = Label(game_frame, image=imgBackground4)
        lb_backgroud.place(x=-190, y=-140)

        lb_card = Label(game_frame, image=imgCard)
        lb_card.place(x=380, y=10, width=214, height=318)

        lb_value = Label(game_frame, font=("Arial", 23), text="Insira um valor:")
        lb_value.configure(background="light green")
        lb_value.place(x=250, y=350)
        insert_value = Entry(game_frame)
        insert_value.place(x=490, y=353, width=250, height=35)

        lb_suit = Label(game_frame, font=("Arial", 23), text="Insira um naipe:")
        lb_suit.configure(background="light green")
        lb_suit.place(x=250, y=430)
        insert_suit = Entry(game_frame)
        insert_suit.place(x=490, y=433, width=250, height=35)

        btnConfirm = Button(game_frame, width=8, height=1, text="Verificar", activebackground="yellow",
                            activeforeground="red")
        btnConfirm.configure(font=("Arial, bold", 18), highlightbackground="yellow", highlightthickness=1, bd=3,
                             foreground="yellow", background="red",
                             command=lambda: verifica_jogada(insert_value.get(), insert_suit.get(), value_random,
                                                             victories, defeats, imgCard_sorted, ls))
        btnConfirm.place(x=410, y=500)

    def verifica_jogada(sv, ss, vr, vi, de, ics, lfs):
        if sv.lower() == vr[0] and ss.lower() == vr[1]:
            initial_frame.place_forget()
            information_frame.place_forget()
            game_frame.place_forget()
            defeats_frame.place_forget()
            points_frame.place_forget()
            reset_frame.place_forget()
            loop_frame.place_forget()
            victories_frame.place(width=980, height=580)
            vi += 1

            lb_backgroud = Label(victories_frame, image=imgBackground5)
            lb_backgroud.place(x=-60, y=0)

            lc = Label(victories_frame, image=ics)
            lc.place(x=380, y=25, width=214, height=318)

            lb_congrulations = Label(victories_frame, font=("Arial", 23),
                                     text="Párabens você acertou a carta secreta!!!")
            lb_congrulations.configure(background="light green")
            lb_congrulations.place(x=200, y=390)

            btnConfirm = Button(victories_frame, width=8, height=1, text="Ok", activebackground="yellow",
                                activeforeground="red")
            btnConfirm.configure(font=("Arial, bold", 18), highlightbackground="yellow", highlightthickness=1, bd=3,
                                 foreground="yellow", background="red", command=lambda: write_points(vi, de))
            btnConfirm.place(x=410, y=500)
        else:
            if lfs == 1:
                initial_frame.place_forget()
                information_frame.place_forget()
                game_frame.place_forget()
                victories_frame.place_forget()
                points_frame.place_forget()
                reset_frame.place_forget()
                loop_frame.place_forget()
                defeats_frame.place(width=980, height=580)
                de += 1

                lb_backgroud = Label(defeats_frame, image=imgBackground6)
                lb_backgroud.place(x=-60, y=0)

                lb_defeat = Label(defeats_frame, font=("Arial", 25), text="Que pena você perdeu.")
                lb_defeat.configure(background="light green")
                lb_defeat.place(x=300, y=250)

                btnConfirm = Button(defeats_frame, width=8, height=1, text="Ok", activebackground="yellow",
                                    activeforeground="red")
                btnConfirm.configure(font=("Arial, bold", 18), highlightbackground="yellow", highlightthickness=1, bd=3,
                                     foreground="yellow", background="red",
                                     command=lambda: write_points(vi, de))
                btnConfirm.place(x=410, y=330)

            initial_frame.place_forget()
            information_frame.place_forget()
            game_frame.place_forget()
            victories_frame.place_forget()
            points_frame.place_forget()
            reset_frame.place_forget()
            defeats_frame.place_forget()
            loop_frame.place(width=980, height=580)
            lfs -= 1

            lb_backgroud = Label(loop_frame, image=imgBackground4)
            lb_backgroud.place(x=-190, y=-140)

            lb_loop1 = Label(loop_frame, font=("Arial", 25),
                             text="O valor " + str(sv.lower()) + " é diferente do valor que foi escolhido.")
            lb_loop1.configure(background="light green")
            lb_loop1.place(x=150, y=140)

            if ss.lower() != vr[1]:
                lb_loop2 = Label(loop_frame, font=("Arial", 25),
                                 text="O naipe tambem é diferente.")
                lb_loop2.configure(background="light green")
                lb_loop2.place(x=280, y=230)

            lb_loop3 = Label(loop_frame, font=("Arial", 25),
                             text="agora lhe resta apenas " + str(lfs) + " vidas.")
            lb_loop3.configure(background="light green")
            lb_loop3.place(x=245, y=320)

            btnConfirm = Button(loop_frame, width=8, height=1, text="Ok", activebackground="yellow",
                                activeforeground="red")
            btnConfirm.configure(font=("Arial, bold", 18), highlightbackground="yellow", highlightthickness=1, bd=3,
                                 foreground="yellow", background="red", command=lambda: Game(lfs))
            btnConfirm.place(x=410, y=420)

    Game(lifes)


def write_points(v, d):
    points = open("points.txt", "r")
    list_points = points.read()
    print(list_points)#Teste
    os.remove("/home/r1/PycharmProjects/pythonProject/CardRandomV2/points.txt")
    file = open("points.txt", "w")
    concat1 = v + int(list_points[0])
    concat2 = d + int(list_points[2])
    file.write(str(concat1) + ";" + str(concat2) + ";" + "Developed by RITKILL\n")
    file.close()
    frameIntroduction()


def show_score():
    initial_frame.place_forget()
    game_frame.place_forget()
    victories_frame.place_forget()
    defeats_frame.place_forget()
    information_frame.place_forget()
    reset_frame.place_forget()
    loop_frame.place_forget()
    points_frame.place(width=980, height=580)

    arqu = open("points.txt", "r")
    score = str(arqu.readlines())

    lb_backgroud = Label(points_frame, image=imgBackground3)
    lb_backgroud.place(x=0, y=0)

    btnVoltar = Button(points_frame, width=7, height=1, text="Voltar", activebackground="yellow",
                       activeforeground="red")
    btnVoltar.configure(font=("Arial, bold", 12), highlightbackground="yellow", highlightthickness=1, bd=3,
                        foreground="yellow", background="red", command=voltar_Login)
    btnVoltar.place(x=30, y=30)

    lb_theme = Label(points_frame, background="light green", foreground="yellow", font=("Arial", 35),
                     text="Game Score")
    lb_theme.place(x=350, y=30)

    lb_victory = Label(points_frame, background="light green", foreground="black", font=("Arial", 28),
                       text="Vitorias: " + str(score[2]))
    lb_victory.place(x=170, y=160)

    lb_defeats = Label(points_frame, background="light green", foreground="black", font=("Arial", 28),
                       text="Derrotas: " + str(score[4]))
    lb_defeats.place(x=170, y=280)


def reset():
    os.remove("/home/r1/PycharmProjects/pythonProject/CardRandomV2/points.txt")
    file = open("points.txt", "w")
    file.write("0;0;Developed by RITKILL\n")
    file.close()


def reset_arquive():
    initial_frame.place_forget()
    game_frame.place_forget()
    victories_frame.place_forget()
    defeats_frame.place_forget()
    points_frame.place_forget()
    information_frame.place_forget()
    loop_frame.place_forget()
    reset_frame.place(width=980, height=580)

    lb_backgroud = Label(reset_frame, image=imgBackground2)
    lb_backgroud.place(x=0, y=0)

    btnVoltar = Button(reset_frame, width=7, height=1, text="Voltar", activebackground="yellow",
                       activeforeground="red")
    btnVoltar.configure(font=("Arial, bold", 12), highlightbackground="yellow", highlightthickness=1, bd=3,
                        foreground="yellow", background="red", command=voltar_Login)
    btnVoltar.place(x=30, y=30)

    lb_caution = Label(reset_frame, background="yellow", foreground="red", font=("Arial", 22),
                       text="Aviso!!!\nEssa ação ira resetar todos os pontos, tem certeza disso?")
    lb_caution.place(x=100, y=220)

    btnReset = Button(reset_frame, width=8, height=1, text="Resetar", activebackground="yellow",
                      activeforeground="red")
    btnReset.configure(font=("Arial, bold", 18), highlightbackground="yellow", highlightthickness=1, bd=3,
                       foreground="yellow", background="red", command=reset)
    btnReset.place(x=390, y=430)


def quit_game():
    window.destroy()


def frameIntroduction():
    reset_frame.place_forget()
    game_frame.place_forget()
    victories_frame.place_forget()
    defeats_frame.place_forget()
    points_frame.place_forget()
    information_frame.place_forget()
    loop_frame.place_forget()
    initial_frame.place(width=980, height=580)

    lb_backgroud = Label(initial_frame, image=imgBackground)
    lb_backgroud.place(x=-60, y=-50, width=1100, height=640)

    frase = Label(initial_frame, font=("Ubuntu", 35), text="Welcome the Card Random!!!")
    frase.configure(background="red", foreground="yellow")
    frase.place(x=180, y=25)

    btnPlay = Button(initial_frame, width=8, height=1, foreground="yellow", background="red",
                     highlightbackground="yellow")
    btnPlay.configure(command=context_game, font=("Arial", 22), activeforeground="red", activebackground="yellow",
                      border=0, bd=3, text="Play")
    btnPlay.place(x=410, y=150)

    btnRecords = Button(initial_frame, width=8, height=1, foreground="yellow", background="red",
                        highlightbackground="yellow")
    btnRecords.configure(command=show_score, font=("Arial", 22), activeforeground="red", activebackground="yellow",
                         border=0, bd=3, text="Records")
    btnRecords.place(x=410, y=250)

    btnReset = Button(initial_frame, width=8, height=1, foreground="yellow", background="red",
                      highlightbackground="yellow")
    btnReset.configure(command=reset_arquive, font=("Arial", 22), activeforeground="red", activebackground="yellow",
                       border=0, bd=3, text="Reset")
    btnReset.place(x=410, y=350)

    btnExit = Button(initial_frame, width=8, height=1, foreground="yellow", background="red",
                     highlightbackground="yellow")
    btnExit.configure(command=quit_game, font=("Arial", 22), activeforeground="red", activebackground="yellow",
                      border=0, bd=3, text="Exit")
    btnExit.place(x=410, y=450)

    lb_credits = Label(initial_frame, font=("Arial", 16), text="Developed By R1TKILL - Versão: 1.0.0",
                       foreground="yellow")
    lb_credits.configure(background="green")
    lb_credits.place(x=300, y=540)


# variables
getImages = os.path.dirname(__file__)
victories = 0
defeats = 0
lifes = 15

# Separating by Suits and values in class.
path = "../CardRandomV2/images"
dirs = os.listdir(path)
cards = []

for i in dirs:
    cards.append(Cards(i.split('_')[0], i.split('_')[1]))

# Main Window.
window = Tk()
window.title("Card Game")
window.geometry("980x580+170+80")
window.resizable(width=False, height=False)

imgBackground = PhotoImage(file=getImages + "/themes/tema1.png")
imgBackground2 = PhotoImage(file=getImages + "/themes/tema2.png")
imgBackground3 = PhotoImage(file=getImages + "/themes/tema5.png")
imgBackground4 = PhotoImage(file=getImages + "/themes/tema_jogo.png")
imgBackground5 = PhotoImage(file=getImages + "/themes/tema_vitoria.png")
imgBackground6 = PhotoImage(file=getImages + "/themes/tema_Derrota.png")
imgCard = PhotoImage(file=getImages + "/themes/reverse_card.png")

# The intro window frames.
initial_frame = Frame(window)
# The game frames.
information_frame = Frame(window)
game_frame = Frame(window)
victories_frame = Frame(window)
defeats_frame = Frame(window)
loop_frame = Frame(window)
# Points frame.
points_frame = Frame(window)
# Reset frame.
reset_frame = Frame(window)

frameIntroduction()
window.mainloop()