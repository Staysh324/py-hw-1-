# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input ("введите число: "))
degree = 0
degreenum = 2
while degreenum < num:
    degreenum = 2 ** degree
    degree += 1
    if degreenum < num:
        print(degreenum)