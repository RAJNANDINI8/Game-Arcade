from tkinter import *
import random

Game_width = 700
Game_Height = 700
Speed = 100
Space_Size = 35
Body_Parts = 3
Snake_Colour = "Green"
Food_Colour = "Red"
Background_colour = "Black"


class Snake:
    def __init__(self):
        self.body_Size = Body_Parts
        self.coordinates = []
        self.square = []

        for i in range(0, Body_Parts):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            squares = canvas.create_rectangle(x, y, x + Space_Size, y + Space_Size, fill=Snake_Colour, tags="Snake")
            self.square.append(squares)


class Food:
    def __init__(self):
        x = random.randint(0, (Game_width / Space_Size) - 1) * Space_Size
        y = random.randint(0, (Game_Height / Space_Size) - 1) * Space_Size

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + Space_Size, y + Space_Size, fill=Food_Colour, tags="food")#To increase size of snake as it eats


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y = y - Space_Size

    elif direction == "down":
        y = y + Space_Size
    elif direction == "right":
        x = x + Space_Size
    elif direction == "left":
        x = x - Space_Size

    snake.coordinates.insert(0, (x, y))

    squares = canvas.create_rectangle(x, y, x + Space_Size, y + Space_Size, fill=Snake_Colour)

    snake.square.insert(0, squares)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score = score + 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.square[-1])

        del snake.square[-1]

    if check_collision(snake):
        game_over()
    else:
        window.after(Speed, next_turn, snake, food)


def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= Game_width:
        return True
    if y < 0 or y >= Game_Height:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER",
                       fill='red', tags="GAME OVER")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)
score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('comsolas', 40))
label.pack()

canvas = Canvas(window, bg=Background_colour, height=Game_Height, width=Game_width)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
scrren_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((scrren_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()  # object of class snake
food = Food()

next_turn(snake, food)

window.mainloop()
