def value_check(value):
    try:
        value = int(value)
        return value
    except ValueError:
        print('Неверный формат ввода \nВведите новое число:')
        value = input()
        return (value_check(value))

print('Введите число:')
value = value_check(input())
print(f'Число {value} в двоичном коде = ', end='')
binary_number = []

while value > 1:
    if value % 2 == 0:
        binary_number.insert(0, 0)
        value /= 2

    if value % 2 != 0:
        binary_number.insert(0, 1)
        value = int(value/2)
        

for i in binary_number:
    print(i, end='')
