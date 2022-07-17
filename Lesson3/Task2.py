import random

list = []

for i in range(3, random.randint(6, 15)):
    list.append(random.randint(0, 15))
print(list)

if len(list) % 2 != 0:
    for i in range(0, len(list)//2):

        multiplication = list[i] * (list[-(i+1)])
        print(multiplication)

    multiplication = list[round(len(list)/2)]**2
    print(multiplication)

else:
    for i in range(0, len(list)//2):

        multiplication = list[i] * (list[-(i+1)])
        print(multiplication)
