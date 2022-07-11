print('Чтобы узнать выходной день или нет, введите день недели числом')
user_date = int(input())
day_week = ['Понедельник.', 'Вторник.', 'Среда.',
            'Четверг.', 'Пятница.', 'Суббота.', 'Воскресенье.']

if user_date == 0 or user_date > 7:
    while True:
        print('Неверно. Попробуйте еще раз')
        user_date = int(input())
        if 7 >= user_date >= 1:
            break

if user_date < 6:
    print(day_week[user_date-1] + ' Этот день - рабочий')
else:
    print(day_week[user_date-1] + ' Этот день - выходной')
