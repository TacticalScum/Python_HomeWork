def value_check(value):
    try:
        value = int(value)
        if int(value) == 0:
            while True:
                print('Числа Фибоначчи для 0 нет.  \nВведите новое число:')
                new_value = int(input())
                if new_value != 0:
                    break
        return value
    except ValueError:
        print('Неверный формат ввода \nВведите новое число:')
        value = input()
        return (value_check(value))

print('Введите число:')
value = value_check(input())
list = [1, 0, 1]

if value == 1 or value == -1:
    print(list[1])
elif value == 2 or value == -2:
    print(list)
else:
    for i in range(3, int(value+1)):
        list.append(list[i-2]+list[i-1])

    for i in range(0, int(value-2)):
        list.insert(0, list[1]-(list[0]))
    print(list)
