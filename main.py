list = []
lista = []
listb = []
for k in range(1,101):
    list.append(k)

for n in list:
    if n>40 and n<60:
        listb.append(n)
    else:
        lista.append(n)
print(lista)
print(listb)
