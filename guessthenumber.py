from tkinter import *
import random
import tkinter as tk

attempts = 10

answer = random.randint(1, 99)


def check_answer():
    global attempts
    global text

    attempts = attempts - 1

    guess = int(entry_window.get())

    if answer == guess:
        text.set("YOU WIN CONGRATS!!")
        tk.Button(text="\U0001f389", font=("", 100)).pack()
        check.pack_forget()

    elif attempts == 0:
        text.set("YOU ARE OUT OF ATTEMPTS")
        tk.Button(text="\U0001F614", font=("", 100)).pack()
        check.pack_forget()

    elif attempts == -1:
        f.destroy()

    elif guess < answer:
        text.set("Oops !! incorrect You have " + str(attempts) + " attempts remaining .Go higher !!")

    elif guess > answer:
        text.set("Oops !! incorrect You have " + str(attempts) + " attempts remaining .Go lower !!")
        return


root = Tk()
root.title("Guess the number")
f = Frame(root, height=1000, width=1000, bg="#008080")
f.propagate(0)
f.pack()

label = Label(f, text="Guess the number between 1 and 99", bg="#C0C0C0", font=('Time', 20))
label.grid(row=0, column=1, padx=33, pady=00)

entry_window = Entry(f, width=30, borderwidth=4, font=('Time', 18))
entry_window.pack(pady=65)

check = Button(f, text="CHECK", height=4, width=15, bg="#C0C0C0", command=check_answer)
check.grid(row=2, column=1, padx=33, pady=85)

quit = Button(f, text="QUIT", width=15, height=2, command=root.destroy)
quit.grid(row=3, column=1, padx=33)
quit.pack(pady=50)

text = StringVar()
text.set("You have 10 attempts remaining!")

guess_attempts = Label(f, textvariable=text, bg="#C0C0C0", font=('Time', 17))
guess_attempts.grid(row=4, column=1, padx=33, pady=40)

root.mainloop()