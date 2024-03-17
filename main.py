a = int(input("введите число:"))
count = 0
while(a > 0):
    count = count + 1
    a = a // 10
    print(count)