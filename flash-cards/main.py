from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = words_data.to_dict(orient = "records")


current_card = {}


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image = card_front)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    flip_timer = window.after(3000, func = flash_card)


def flash_card():
    canvas.itemconfig(card, image = card_back)
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")


def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_word()


window = Tk()
window.title("Flash Card Game")
window.config(padx = 50, pady = 20, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flash_card)

canvas = Canvas(width = 800, height = 550, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_back = PhotoImage(file = "./images/card_back.png")
card_front = PhotoImage(file = "./images/card_front.png")
right = PhotoImage(file = "./images/right.png")
wrong = PhotoImage(file = "./images/wrong.png")

card = canvas.create_image(400, 275, image = card_front)
canvas.grid(column = 0, row = 0, columnspan = 2)
card_title = canvas.create_text(400, 150, text = "", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 275, text = "", font = ("Ariel", 60, "bold"))

right_button = Button(image = wrong, highlightthickness = 0, command = is_known)
right_button.grid(column = 0, row = 1)

wrong_button = Button(image = right, highlightthickness = 0, command = next_word)
wrong_button.grid(column = 1, row = 1)

next_word()

window.mainloop()
