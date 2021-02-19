from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width = 200, height = 100)
window.config(padx = 50, pady = 25)

input = Entry(width = 10)
input.grid(column = 1, row = 0)

mile_label = Label(text = "Miles", font = ("Arial", 14))
mile_label.grid(column = 2, row = 0)

equal_label = Label(text = "is equal to", font = ("Arial", 14))
equal_label.grid(column = 0, row = 1)

result_label = Label(text = "", font = ("Arial", 14))
result_label.grid(column = 1, row = 1)

km_label = Label(text = "Km", font = ("Arial", 14))
km_label.grid(column = 2, row = 1)


def button_click():
    result_label["text"] = round(int(input.get()) * 1.60934)


button = Button(text = "Calculate", command = button_click)
button.grid(column = 1, row = 3)

window.mainloop()
