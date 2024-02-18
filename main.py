name="Костя"
age="15"
num="96"
print("меня зовут",name,"мне",age,"учусь в школе номер",num)

K = int(input("Введи число K: "))
N = int(input("Введи число N: "))

if K<N :
    for i in range(K + 1, N):
        print(i)
else:
    for i in range(N + 1, K):
        print(i)