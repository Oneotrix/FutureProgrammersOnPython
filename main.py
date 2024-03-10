list = ["23","","я кутой","32","","хыхы"]
d = 0
for i in list:
    if i =="":
        list.pop(d)
    d += 1
print(list)