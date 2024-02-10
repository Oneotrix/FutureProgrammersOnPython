low = int(input("введите нижнею границу деапозона "))
high = int(input("введите вернюю границу деапозона "))
a = []
for x in range(low, high + 1):
    i = 2
    while x % i != 0:
        i += 1
    if i == x:
        a.append(x)
print(a)