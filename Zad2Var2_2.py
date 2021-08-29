from random import randrange
a = int(input("Кол-во столбцов: "))
b = int(input("Кол-во строк: "))
tabl = [[int(c) for c in [randrange(0, 10) for _ in range(a)]] for _ in range(b)]
print()
for x in range(b):
    for z in range(a):
        print(str(tabl[x][z]).rjust(1), end=' ')
    print()

max_sum = [sum(c) for c in tabl]

print('Номер строки, сумма чисел в которой максимальна: ', max_sum.index(max(max_sum)) + 1)
