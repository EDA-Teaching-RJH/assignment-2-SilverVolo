### Part Three -- your code goes here. 
list = [3,1,4,1,5,9,2,6,5,3]
list.sort()
x = list.count(1)
for i in range(0,x):
    list.remove(1)
list.append(7)
list.append(8)
print(list)
