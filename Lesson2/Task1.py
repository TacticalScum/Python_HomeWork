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
user_value = input()
value_sum = 0
clear_value = str(value_check(user_value))

for i in clear_value:
    if i == '.':
        value_sum += 0
    else:
        value_sum += int(i)

print(value_sum)
