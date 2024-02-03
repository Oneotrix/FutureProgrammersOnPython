N = int(input("Ведите чило N: "))
count = 0
for i in range(1, N + 1):
    num = int(input("Ведите число: "))
    if num == 0:
        count = count + 1
print(count)