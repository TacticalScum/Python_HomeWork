def value_check(value):
    try:
        value = float(value)
        return value
    except ValueError:
        print('Неверный формат ввода')
        print('Введите новое число:')
        value = input()
        return (value_check(value))


print('Введите число:')
user_value = str(value_check(input()))
value_sum = 0

for i in clear_value:
    if i == '.':
        value_sum += 0
    else:
        value_sum += int(i)

print(value_sum)