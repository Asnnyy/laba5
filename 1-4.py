import random


def z1():
    spisok = [1, 5, 10, 15, 20]
    chislo = int(input("Введте Ваше число"))
    if chislo in spisok:
        print("Поздравляю! Вы угадали число")
    else:
        print("Нет такого числа")
z1()

def z2():
    spisok = ["cat", "dog", "snake", "cat", "alligator"]
    s = filter(lambda x: spisok.count(x) > 1, spisok)
    s = list(set(s))
    print(s)
z2()

def z3():
    d = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    otv = int(input("Сколько Вы хотите выходных?"))
    print(d[-otv:7])
    print(d[0:-otv])
z3()

def z4():
    l1 = ["pupkin", "petrov", "ivanov", "semenov", "kuznetsov", "smirnov", "popov", "sokolov","kozlov", "morozov"]
    l2 = ["volkov", "zaytsev", "pavlov", "tarasov", "belov", "orlov", "titov", "polyakov", "sidorov", "antonov"]
    team0 = (l1[0:5] + l2[0:5])
    d = len(team0)
    ts = sorted(team0)
    print(l1, l2, team0, d, ts)
    a = "ivanov"
    s = team0.count(a)
    if a in team0:
        print("В команде имеется такой игрок/и", ";", "Эта фамилия встречается:", s)
    else:
        print("Такого тгрока нет в команде")
z4()
