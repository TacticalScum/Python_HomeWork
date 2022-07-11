def value_check(value):
    if value > 1:
     while True:
        print('Неверно. Попробуйте еще раз')
        new_value = int(input())
        if new_value < 1:
            break
        
        
print('Введите X = ')
x = int(input())
value_check(x)

print('Введите Y = ')
y = int(input())
value_check(y)

print('Введите Z = ')
z = int(input())
value_check(z)

left = not(x or y or z)
right = not x and not y and not z
result = left == right

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')



