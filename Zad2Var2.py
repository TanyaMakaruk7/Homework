P = int(input('Выручка фирмы\n'))
Q = int(input('Выручка за день \n'))
counter = 0
while Q <= P:
    print(Q)
    I = Q * 0.03
    Q = Q + I
    counter += 1
print(F"Надо торговать фирме {counter+1} дней для достижения необходимой выручки ")