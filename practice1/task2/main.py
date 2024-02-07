# Gamzat Shakhmanaev

from tkinter import *
from tkinter import messagebox
import os


def get_results():
    arg_x = int(arg_x_tf.get())
    arg_y = int(arg_y_tf.get())

    os.system(f"./Equation {arg_x} {arg_y} >> res.txt")

    with open('res.txt') as f:
        res = f.readline()
    
    os.system("rm res.txt")
    
    messagebox.showinfo('Результат', f"Результат уравнения = {res}")


window = Tk()
window.title("Решение уравнение №2")
window.geometry("600x500")

frame = Frame(
    window, 
    padx = 10,
    pady = 10
)
frame.pack(expand=True)

arg_x_lb = Label(
    frame,
    text="Введите X"
)
arg_x_lb.grid(row=3, column=1)

arg_y_lb = Label(
    frame,
    text="Введите Y"
)
arg_y_lb.grid(row=4, column=1)

arg_x_tf = Entry(
    frame,
)
arg_x_tf.grid(row=3, column=2)

arg_y_tf = Entry(
    frame
)
arg_y_tf.grid(row=4, column=2, pady=5)

result_button = Button(
    frame,
    text="Вычислить результат",
    command=get_results
)
result_button.grid(row=5, column=2)

window.mainloop()
