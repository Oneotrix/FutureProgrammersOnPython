n = int(input("Ввидите числ0"))
list = []
for i in range(1,n):
    list.append(i)
new_list = list[0:n-10]
print(new_list)