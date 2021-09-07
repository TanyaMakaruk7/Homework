a = int(input('Введите длину а: '))
b = int(input('Введите ширину b: '))
size = []
count = 0
def square(a, b, count):
    if a == b:
        size.append(a)
        return a, count + 1
    elif a < b:
        size.append(a)
        return square(a, b - a, count + 1)
    else:
        size.append(b)
        return square(b, a - b, count + 1)
q = square(a, b, count)
len = " ".join(str(size))
print("Длина ребер получаемых квадратов:"+len)
print("Кол-во полученых квадратов: " + str(q[-1]))