list = [1,2,3,4,5,6,7,8,9,10]
count = 0
size = 0

list.__len__()

for i in  range(1, list.__len__()):
    if list[i] > list[i-1]:
        count +=1

print(count)