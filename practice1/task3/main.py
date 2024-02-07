# Gamzat Shakhmanaev

from tkinter import *
from tkinter import messagebox
import os


def get_results():
    height = int(height_tf.get())
    width = int(width_tf.get())

    os.system(f"./Rectangle {height} {width} >> res.txt")

    with open('res.txt') as f:
        square = f.readline()
        perimeter = f.readline()
    
    os.system("rm res.txt")
    
    messagebox.showinfo('Результат', f"Площадь: {square} Периметр: {perimeter}")


window = Tk()
window.title("Калькулятор площади и периметра прямоугольника/квадрата")
window.geometry("600x500")

frame = Frame(
    window, 
    padx = 10,
    pady = 10
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="Введите высоту прямоугольника"
)
height_lb.grid(row=3, column=1)

width_lb = Label(
    frame,
    text="Введите ширину"
)
width_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2)

width_tf = Entry(
    frame
)
width_tf.grid(row=4, column=2, pady=5)

result_button = Button(
    frame,
    text="Рассчитать площадь и периметр",
    command=get_results
)
result_button.grid(row=5, column=2)

window.mainloop()
