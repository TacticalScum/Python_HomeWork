import math

def value_check(value):
    try:
        value = int(value)
        return value
    except ValueError:
        print('Неверный формат ввода \nВведите новое число:')
        value = input()
        return (value_check(value))

print('До какого знака высчитать число pi?')
value = value_check(input())

if value == 0:
    print('Число pi = 3')
else:
 print('Число pi = ', end='')
 print(round(math.pi, value))
