a = int (input())
b = int (input())
c = int (input())
if a+b<c and a+c<b and b+c<a:
    print("сумма любых 2ух сторон треугольников должна быть > длины третей стороны")
    exit()
p = a+b+c
p1 =(a+b+c)/2
s = p1*(p1-a)*(p1-b)*(p1-c)**0.5
print(p)
print(s)
