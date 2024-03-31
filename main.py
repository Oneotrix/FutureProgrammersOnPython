list=[]
for i in range(0,100):
    list.append(i)
size=0
sum=0
for i in list:
    size=size+1
    sum=sum+i
result=sum/size
print(result)
