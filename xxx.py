people = []
stop = ""
while stop != "Всё" :

    print("Привет. Кто идёт бухать?")
    name = input()
    print("Что будет пить?")
    drink = input()
    print("До скольки будет тусить?")
    reiv = input()
    nam = "Имя"
    dr = "Пьёт"
    re = "Будет тусить до"

    spisok = {nam: name, dr: drink, re: reiv}
    people.append(spisok)
    print("Кто то ещё?")
    proverka = input()
    if proverka == "Нет":
        break


for xx in people:
    first = xx
    qq = list(xx.values())[0]
    print(qq)