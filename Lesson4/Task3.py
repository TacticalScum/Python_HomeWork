import random
import os
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           }

degrees = []
x = []
for i in range(0, 20):
    degrees.append(random.randint(0, 100))
print(degrees)

filepath = os.path.join
data = open('Task3_degrees.txt', 'w', encoding="utf-8")

for i in range(0, 20):
    ind = ""
    for char in str(degrees[i]):
        ind += indexes[char]
    data.writelines(f'10 * x{ind} = 0\n')
    
data.close