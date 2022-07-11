def value_check(value):
    if value == 0:
     while True:
        print('Неверно. Попробуйте еще раз')
        new_value = int(input())
        if new_value != 0:
            break
        
        
print('Введите X = ')
x = int(input())
value_check(x)

print('Введите Y = ')
y = int(input())
value_check(y)

if x>0 and y>0:
    print('Точка находится в I четверти')
elif x>0 and y<0:
    print('Точка находится вo II четверти')
elif x<0 and y<0:
    print('Точка находится в III четверти')
elif x<0 and y>0:
    print('Точка находится в IV четверти')