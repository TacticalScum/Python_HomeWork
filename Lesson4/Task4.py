import os

list_degrees1 = []
list_degrees2 = []

file_degrees1 = open('c:/Users/babus/Desktop/Python/Lesson4/task3_degree1.txt',
                     'r', encoding="utf-8")
for line in file_degrees1:
    list_degrees1.append(line)

file_degrees2 = open('c:/Users/babus/Desktop/Python/Lesson4/task3_degree2.txt',
                     'r', encoding="utf-8")
for line in file_degrees2:
    list_degrees2.append(line)


filepath = os.path.join(
    'c:/Users/babus/Desktop/Python/Lesson4', 'task4_sum.txt')
sum_degrees = open(filepath, 'w', encoding="utf-8")

for i in range(0, 20):
    for j in list_degrees1[i]:
        if j == '=':
            break
        sum_degrees.writelines(j)
    sum_degrees.writelines(f'+ {list_degrees2[i]}\n')


file_degrees1.close
file_degrees2.close
sum_degrees.close
