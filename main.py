list = []

n = int(input("длина списка:"))

for i in range (0, n):
    list.append(i)

print(list[0:n-1])