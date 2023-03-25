from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Scissor Paper")
root.configure(bg="#9b59b6")
# picture
rock_left = ImageTk.PhotoImage(Image.open("rock1right.png"))
rock_right = ImageTk.PhotoImage(Image.open("rock1left.png"))
paper_left = ImageTk.PhotoImage(Image.open("paper1right.png"))
paper_right = ImageTk.PhotoImage(Image.open("paper1left.png"))
scissor_left = ImageTk.PhotoImage(Image.open("scissor1right.png"))
scissor_right = ImageTk.PhotoImage(Image.open("scissor1left.png"))

left_label = Label(root, image=scissor_right, bg="#9b59b6")
right_label = Label(root, image=scissor_left, bg="#9b59b6")
right_label.grid(row=1, column=0)
left_label.grid(row=1, column=4)

# scores
leftScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
rightScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
rightScore.grid(row=1, column=1)
leftScore.grid(row=1, column=3)

# indicators
left_indicator = Label(root, font=50, text="COMPUTER")
right_indicator = Label(root, font=50, text="USER")
left_indicator.grid(row=0, column=3)
right_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# update choices
choices = ["rock", "paper", "scissor"]


def update(x):
    # for computer
    compChoice = choices[random.randint(0, 2)]
    if compChoice == "rock":
        left_label.configure(image=rock_right)
    elif compChoice == "paper":
        left_label.configure(image=paper_right)
    else:
        left_label.configure(image=scissor_right)

    # for user
    if x == "rock":
        right_label.configure(image=rock_left)
    elif x == "paper":
        right_label.configure(image=paper_left)
    else:
        right_label.configure(image=scissor_left)
    checkwin(x, compChoice)


# update message
def updateMessage(x):
    msg['text'] = x


# update user score
def updateUserScore():
    score = int(rightScore["text"])
    score = score + 1
    rightScore["text"] = str(score)


# update computer score
def updateComputerScore():
    score = int(leftScore["text"])
    score = score + 1
    leftScore["text"] = str(score)


# check winner
def checkwin(user, computer):
    if user == computer:
        updateMessage("ITS A TIE !!!")
    elif user == "rock":
        if computer == "paper":
            updateMessage("You loose !!!")
            updateComputerScore()
        else:
            updateMessage("You win !!!")
            updateUserScore()

    elif user == "paper":
        if computer == "scissor":
            updateMessage("You loose !!!")
            updateComputerScore()
        else:
            updateMessage("You win !!!")
            updateUserScore()
    elif user == "scissor":
        if computer == "rock":
            updateMessage("You loose !!!")
            updateComputerScore()
        else:
            updateMessage("You win !!!")
            updateUserScore()
    else:
        pass


# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E40", fg="white", command=lambda: update("rock"))
rock.grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: update("paper"))
paper.grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: update("scissor"))
scissor.grid(row=2, column=3)

root.mainloop()
