list = [10, 5, 13, 21, 42, 51, 61]
count = 0
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        count += 1
print(count)