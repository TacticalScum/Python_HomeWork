import random

list = list(range(1, 100, 8))
print (f'Исходный массив:\n{list}')

random.shuffle(list)
print (f'Перемешанный массив:\n{list}')