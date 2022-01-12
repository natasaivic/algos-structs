import random

lista = []
n = 5

for i in range(n):
    lista.append(random.randint(-100, 100))

index = 0
max = lista[index]
for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]
        index = i

print(f"For list: {lista}, max element is: {max} at index: {index}")