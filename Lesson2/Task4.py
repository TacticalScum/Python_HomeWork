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

for i in range(-number_n, number_n+1):
    list.append(i)

print('Введите индексы через пробел, чтобы перемножить их.\nПомните! Индексация начинается с нуля.')
index_list = []
x = 1

while True:
     try:
         for i in map(int,input().split()):
          x = x * (list[i])
     except ValueError:
         print('Неверный формат ввода \nВведите новые индексы:')
     else: break
    
print(list)
print(x)
