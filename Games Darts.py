import tkinter as tk
import time
import random

#Перечисление возможных очков
x1 = [i for i in range(1, 21)] + [50]  # Номинальные очки
x2 = [i*2 for i in range(1, 21)] # Удвоенные очки
x3 = [i*3 for i in range(1, 21)] # Утроенные очки
score = x1+x2+x3 #Все очки.

#Здесь хранятся очки из 10 попыток
num = []

#Это для сортировки и разворота наших очков из 10 попыток. Для упрощения
# выявления 3х лучших бросков 
def sorta():
    num.sort()   
    num.reverse() 

#Начинаем кидать дартс. 10 попыток
for xxx in range(10):
    xxx = random.choice(score)
    num.append(xxx)    

#Код из гпк. Одновляет экран добавляя новое очко очередной попытки броска
def update_list():
    for item in num:             
        listbox.insert(tk.END, item)
        listbox.update()
        time.sleep(1)  # Пауза в 1 секунду
            

window = tk.Tk()
window.geometry("400x300")
window.title("Игра в дартс")
listbox = tk.Listbox(window)
listbox.pack()

update_list()
sorta()

#Выводим 3 лучших броска
listw = tk.Label(window,text="Лучшие попытки"+str(num[0:3]))
listw.place(x=200, y=200, anchor="center")
print("Пора спать")



window.mainloop()