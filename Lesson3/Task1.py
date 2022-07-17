import random

list = []
sum = 0

for i in range(3, random.randint(6, 15)):
    list.append(random.randint(0, 15))

print(list)

print('Числа стоящие на нечетных местах: ', end='')
for i in range(len(list)):
    if i % 2 != 0:
        sum = sum + list[i]
        print(list[i], end=', ')

print()
print('Сумма этих чисел = ' + str(sum))
