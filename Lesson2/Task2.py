def value_check(value):
    try:
        value = int(value)
        return value
    except ValueError:
        print('Неверный формат ввода')
        print('Введите новое число:')
        value = input()
        return (value_check(value))


print('Введите число:')
number_n = value_check(input())
list = [1]

for i in range(2, number_n+1):
    list.append(i*(list[i-2]))

print(list)
