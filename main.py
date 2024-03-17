b = 0

a = int(input("введите число:"))

if  a > 0:
    b = b + 1
    a = a // 10
    print(a)
else:
    print(a)