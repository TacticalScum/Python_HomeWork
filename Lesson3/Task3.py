import random

list = []

for i in range(3, random.randint(6, 15)):
    list.append(round(random.random(), 1))
print(list)

decimal_max = list[0] % 10
decimal_min = list[1] % 10


for i in range(0, len(list)):
    if decimal_max < list[i]:
        decimal_max = list[i]
    if decimal_min > list[i]:
        decimal_min = list[i]
print (f'Наибольшая десятичная часть списка: {decimal_max}')
print (f'Наименьшая десятичная часть списка: {decimal_min}')
print((f'Разница между ними = {round (decimal_max-decimal_min, 1)}'))