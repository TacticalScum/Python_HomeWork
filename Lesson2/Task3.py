def value_check(value):
    try:
        value = int(value)
        return value
    except ValueError:
        print('Неверный формат ввода \nВведите новое число:')
        value = input()
        return (value_check(value))


print('Введите число:')
number_n = value_check(input())
sum = 0
list = []

for i in range(1, number_n+1):
    list.append(round(((1+1/i)**i), 3))
    sum = sum + list[i-1]

print(list)
print(sum)
