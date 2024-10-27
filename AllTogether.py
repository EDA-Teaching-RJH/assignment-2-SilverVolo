### Part Four -- your code goes here.
import random

list = []
for i in range(0, 10):
    list.append(random.randint(1, 100))
print(list)
flag = True
while flag:
    index = 0
    for i in range(0, len(list)):

        if list[index] % 2 == 0:
            list.pop(index)
            index -= 1
        index += 1
    flag = False
print(list)