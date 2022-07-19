import random

list = []
unique_list = []

for i in range(0, 10):
    list.append(random.randint(0,10))
print(f'Исходный массив: {list}')

for i in range(0, len(list)):
    if list.count(list[i]) == 1:
     unique_list.append(list[i])
print(f'Массив с неповторяющимися элементами: {unique_list}')