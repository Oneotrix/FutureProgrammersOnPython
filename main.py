
N = int(input("Введите число N: "))

count = 0

for i in range(1, N + 1):
    num = int(input("Введите число: "))
    if(num == 0):
        count = count + 1
print(count)

