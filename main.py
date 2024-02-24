list = []

for i in range(2000, 2301):
    if i % 7 == 0 and i % 5 != 0:
        list.append(str(i))

result = ' '.join(list)
print(result)