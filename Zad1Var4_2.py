import random
n=int(input('Сколько элементом нужно в спике: \n'))
A=[]
C=1
for i in range(n):
    a=random.randint(1,100)
    A.append(a)
    if i%2==1:
        C*=A[i]
print('Элементы списка')
print(A)
print('произведение элементов списка с нечетными номерами \n')
print(C)
m=max(A)
print('наибольший элемент списка \n')
print(m)
A.remove(m)
print('новый список \n')
print(A)