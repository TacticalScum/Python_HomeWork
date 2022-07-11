import math
def value_check(value):
    if value == 0:
        while True:
            print('Неверно. Попробуйте еще раз')
            new_value = int(input())
            if new_value != 0:
                break


print('Введите координату X1 = ')
x1 = int(input())
value_check(x1)
print('Введите координату Y1 = ')
y1 = int(input())
value_check(y1)

print('Введите координату X2 = ')
x2 = int(input())
value_check(x2)
print('Введите координату Y2 = ')
y2 = int(input())
value_check(y2)

length = round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 3)
print(f'Расстояние между точками = {length}')
