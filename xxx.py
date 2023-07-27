import tkinter as tk
import random

def move_no_label():
    x = random.randint(0, width-200)
    y = random.randint(0, height-100)
    no_label.place(x=x, y=y)

def close_window():
    window.destroy()

def on_hover(event):
    move_no_label()
window = tk.Tk()
window.title("Уведомление")
width, height = 400, 200
window.geometry(f"{width}x{height}")

def exitt():
    window = tk.Tk()
    window.title("Уведомление")
    width, height = 400, 200
    window.geometry(f"{width}x{height}")
    notification_label = tk.Label(window, text="Мы не сомневались", font=("Arial", 20))
    notification_label.place(relx=0.5, rely=0.5, anchor="center")


notification_label = tk.Label(window, text="Довольны ли вы \n\nсвой зарплатой?", font=("Arial", 15))
notification_label.place(x=130, y=10)

notification_label = tk.Button(window, text="Да", font=("Arial", 20),command=exitt)
notification_label.place(x=130, y=80)


root = no_label = tk.Button(window, text="Нет", font=("Arial", 20), fg="red")
no_label.place(x=230, y=80)
root.bind("<Enter>", on_hover) 


#root = tk.Tk()
#root.bind('<Enter>', on_hover)


window.mainloop()