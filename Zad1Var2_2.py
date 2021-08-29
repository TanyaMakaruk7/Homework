from random import randrange
numbers = [randrange(0, 10) for _ in range(int(input('Сколько элементом нужно в спике: \n')))]
print('Элементы списка', numbers)
print('Наибольший нечетный элемент:', max([i for i in numbers if i % 2 != 0]))
print('Минимальный по модулю элемент списка:', min([abs(i) for i in numbers]))