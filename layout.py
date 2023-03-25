import os
from tkinter import *
from PIL import ImageTk, Image


class Form:
    def __init__(self, root):
        self.f = Frame(root, height=1000, width=1000)  # frame applied on the root
        self.f.propagate(False)  # to avoid frame shrink
        self.f.pack()
        self.img1 = PhotoImage(file='snake.png')
        self.img2 = PhotoImage(file='rockpaperscissors.png')
        self.img3 = PhotoImage(file='tictactoe.png')
        self.img4 = PhotoImage(file='guess.png')
        imgl1 = Label(image=self.img1)
        imgl2 = Label(image=self.img2)
        imgl2 = Label(image=self.img3)
        self.b1 = Button(self.f, text="Snake", width=238, height=212, bg='light blue', image=self.img1,
                         command=lambda: self.buttonClick(1))
        self.b2 = Button(self.f, text="Rock paper Scissor", width=225, height=225, bg='light pink', image=self.img2,
                         command=lambda: self.buttonClick(2))
        self.b3 = Button(self.f, text="Tic Tac Toe", width=238, height=212, bg='light yellow', image=self.img3,
                         command=lambda: self.buttonClick(3))
        self.b4 = Button(self.f, text="Guess the Number", width=238, height=212, bg='red', image=self.img4,
                         command=lambda: self.buttonClick(4))
        '''self.b1.pack()

        self.b2.pack()
        self.b3.pack()
        self.b4.pack()'''
        self.b1.grid(row=0, column=0, padx=10, pady=25)
        self.b2.grid(row=0, column=1, padx=10, pady=25)
        self.b3.grid(row=1, column=0, padx=10, pady=25)
        self.b4.grid(row=1, column=1, padx=10, pady=10)

    def buttonClick(self, num):
        if num == 1:
            self.f["bg"] = "light blue"
            #self.b1["text"] = " You are playing Snake!"
            # exec('snake.py')
            os.system('python snake.py')

        if num == 2:
            self.f["bg"] = "light pink"
            #self.b2["text"] = "You are playing Rock paper Scissor!"
            os.system('python rockpaperscissor.py')

        if num == 3:
            self.f["bg"] = "Light yellow"
            #self.b3["text"] = "You are playing Tic Tac Toe!"
            os.system('python tictactoe.py')

        if num ==4:
            self.f["bg"]="red"
            #self.b4["text"]=" You are playing Guess the number!"
            os.system('python guessthenumber.py')


root = Tk()
root.title = Label(text="Welcome to the Gaming Arcade!", font=('Comic Sans', 36))
root.configure(bg='aquamarine4')
root.title.pack()
root.geometry("1000x1000")
myForm = Form(root)
root.mainloop()
