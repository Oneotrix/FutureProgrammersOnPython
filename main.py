list=[]
list1=[]
for i in range(1,101):
    list.append(i)
for i in list:
    if i>40 and i<60:
        list.remove(i)
        list1.append(i)
print(list)
print(list1)