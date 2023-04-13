# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть

numcoins = int(input("введите количество монет: "))
tails = 0
for i in range (numcoins):
    inputside = int (input(f"укажите какой стороной лежит монета {i+1}, 1 - решка, 0 - герб: "))
    if (inputside != 0) and (inputside != 1):
        print ("введено неверное значение стороны, монета не будет учтена")
    elif inputside == 1:
            tails += 1
crest = numcoins - tails
if crest < tails:
    print(f"необходимо перевернуть {crest} монет с гербом")
else:
    print(f"необходимо перевернуть {tails} монет с решкой")