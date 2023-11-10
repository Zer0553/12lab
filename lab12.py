# 22. Вычислить сумму знакопеременного ряда |х*(2n+1)!|/(2n+1)!, где х-матрица ранга к (к и матрица задаются случайным
# образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после
# запятой. У алгоритма д.б. линейная сложность. Знак первого слагаемого  -.

import random
import numpy as np
from math import factorial


def make_matrix(t):
    k = random.randint(2, 6)
    n = []
    for i in range(k):
        n.append([])
        for j in range(k):
            n[i].append(random.choice([-1, 1]))
    matrix = np.array(n)
    if abs(np.linalg.det(n)) == 0:
        return make_matrix(t)
    else:

        return matrix


def Line(t):
    matrix = make_matrix(t)
    print("Начальная матрица: ")
    print(matrix)
    answ = 0.0
    n = 1
    flag = True

    while flag:
        try:
            matrix = matrix * factorial(2 * n + 1)
            answ += ((-1) ** n) * (abs(np.linalg.det(matrix)) / factorial(2 * n + 1))
            n += 1
            if len(str(answ).split('.')[1]) > t:
                flag = False
            elif str(answ).find('e') != -1:
                try:
                    flag = (len(str(answ).split('.')[1]) + int(str(answ).split('-')[1])) < t
                except:
                    flag = (len(str(answ).split('.')[1]) + int(str(answ).split('+')[1])) < t
        except np.core._exceptions.UFuncTypeError:
            print('Числа в матрице вышли слишком большими')
            print('Для повторного апуска напишите новое число :')
            return
    print('финальный вид матрицы:')
    print(matrix)
    print('Суммa знакопеременного ряда |х*(2n+1)!|/(2n+1)! :')
    print(answ)
    print('Для повторного апуска напишите новое число :')


print('Введите t - кол-во знаков после запятой: ')
while True:
    try:
        Line(int(input()))
    except ValueError:
        print('Введите чилсло')
