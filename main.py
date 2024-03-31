a = int(input("введите число:"))
b = int(input("введите число:"))
c = int(input("введите число:"))

int1 = a+b > c
int2 = c+b > a
int3 = a+c > b

P = 0
S = 0
p = 0

if int1 and int2 and int3:
    P = a + b + c
    p = P / 2
    S = p * (p - a) * (p - b) * (p - c) ** 0, 5
    print(P)
    print(S)
else:
    print("дебилыч, переделывай")

