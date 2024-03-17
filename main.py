a=int(input("Введите число "))
count=0
while a:
    count+=a%10
    a//=10
print(count)