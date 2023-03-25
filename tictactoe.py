from tkinter import *
import tkinter.messagebox
from turtle import clear

root = Tk()
root.title('Tic Tac Toe')
root.resizable(False, False)
click = True
count = 0
b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()
b5 = StringVar()
b6 = StringVar()
b7 = StringVar()
b8 = StringVar()
b9 = StringVar()

xPhoto = PhotoImage(file='X1.png')
oPhoto = PhotoImage(file='O3.png')


def play():
    # other styles like ridge: raised,sunken,flat,solid,groove
    button1 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b1,
                     command=lambda: press(1, 0, 0))
    button1.grid(row=0, column=0)
    button2 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b2,
                     command=lambda: press(2, 0, 1))
    button2.grid(row=0, column=1)
    button3 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b3,
                     command=lambda: press(3, 0, 2))
    button3.grid(row=0, column=2)
    button4 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b4,
                     command=lambda: press(4, 1, 0))
    button4.grid(row=1, column=0)
    button5 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b5,
                     command=lambda: press(5, 1, 1))
    button5.grid(row=1, column=1)
    button6 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b6,
                     command=lambda: press(6, 1, 2))
    button6.grid(row=1, column=2)
    button7 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b7,
                     command=lambda: press(7, 2, 0))
    button7.grid(row=2, column=0)
    button8 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b8,
                     command=lambda: press(8, 2, 1))
    button8.grid(row=2, column=1)
    button8 = Button(root, height=9, width=19, relief='ridge', borderwidth=0.5, background='#ffe6e6', textvariable=b9,
                     command=lambda: press(9, 2, 2))
    button8.grid(row=2, column=2)


def press(num, r, c):
    global count, click

    if click == True:
        labelPhoto = Label(root, image=xPhoto)
        labelPhoto.grid(row=r, column=c)

        if num == 1:
            b1.set('X')
        elif num == 2:
            b2.set('X')
        elif num == 3:
            b3.set('X')
        elif num == 4:
            b4.set('X')
        elif num == 5:
            b5.set('X')
        elif num == 6:
            b6.set('X')
        elif num == 7:
            b7.set('X')
        elif num == 8:
            b8.set('X')
        else:
            b9.set('X')
        count = count + 1

        click = False
        checkwin()
    else:
        labelPhoto = Label(root, image=oPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            b1.set('O')
        elif num == 2:
            b2.set('O')
        elif num == 3:
            b3.set('O')
        elif num == 4:
            b4.set('O')
        elif num == 5:
            b5.set('O')
        elif num == 6:
            b6.set('O')
        elif num == 7:
            b7.set('O')
        elif num == 8:
            b8.set('O')
        else:
            b9.set('O')
        count = count + 1

        click = True
        checkwin()


def checkwin():
    global count, click
    if ((b1.get() == 'X' and b2.get() == 'X' and b3.get() == 'X') or
            (b1.get() == 'X' and b2.get() == 'X' and b3.get() == 'X') or
            (b4.get() == 'X' and b5.get() == 'X' and b6.get() == 'X') or
            (b7.get() == 'X' and b8.get() == 'X' and b9.get() == 'X') or
            (b1.get() == 'X' and b4.get() == 'X' and b7.get() == 'X') or
            (b2.get() == 'X' and b5.get() == 'X' and b8.get() == 'X') or
            (b3.get() == 'X' and b6.get() == 'X' and b9.get() == 'X') or
            (b1.get() == 'X' and b5.get() == 'X' and b9.get() == 'X') or
            (b3.get() == 'X' and b5.get() == 'X' and b7.get() == 'X')):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Player X Wins !!!")
        click = True
        count = 0
        clear()
        play()

    else:
        if ((b1.get() == 'X' and b2.get() == 'X' and b3.get() == 'X') or
                (b1.get() == 'O' and b2.get() == 'O' and b3.get() == 'O') or
                (b4.get() == 'O' and b5.get() == 'O' and b6.get() == 'O') or
                (b7.get() == 'O' and b8.get() == 'O' and b9.get() == 'O') or
                (b1.get() == 'O' and b4.get() == 'O' and b7.get() == 'O') or
                (b2.get() == 'O' and b5.get() == 'O' and b8.get() == 'O') or
                (b3.get() == 'O' and b6.get() == 'O' and b9.get() == 'O') or
                (b1.get() == 'O' and b5.get() == 'O' and b9.get() == 'O') or
                (b3.get() == 'O' and b5.get() == 'O' and b7.get() == 'O')):
            tkinter.messagebox.showinfo("Tic Tac Toe", "Player O Wins !!!")
            # click = True
            count = 0
            clear()
            play()
        elif count == 9:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Tie game !!!")
            clear()
            play()


def clear():
    b1.set("")
    b2.set("")
    b3.set("")
    b4.set("")
    b5.set("")
    b6.set("")
    b7.set("")
    b8.set("")
    b9.set("")


play()
root.mainloop()
