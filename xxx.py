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

first = people[0]
key = list(first.values())[0]
print(key)