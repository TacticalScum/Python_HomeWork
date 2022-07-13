def value_check(value):
    try:
        value = float(value)
        return value
    except ValueError:
        print('Неверный формат ввода \nВведите новое число:')
        value = input()
        return (value_check(value))


print('Введите число:')
user_value = str(value_check(input()))
value_sum = 0

for i in user_value:
    if i.isdigit() == True:
         value_sum += int(i)

print(value_sum)
