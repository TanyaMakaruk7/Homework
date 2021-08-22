import random
n = int(input('Сколько элементом нужно в спике: \n'))
A=[]
for i in range(n):
    A.append(random.randint(0,99))
print('Элементы списка')
print(A)
print('Максимальное значение в списке ' + str(max(A)))