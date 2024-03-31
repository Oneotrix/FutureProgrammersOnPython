a = int (input())
b = int (input())
c = int (input())
if a+b<c or b+a<c or a+c<b or c+a<b or b+c<a or c+b<a:
    print("сумма любых 2ух сторон треугольников должна быть > длины третей стороны")
    exit()
p = a+b+c
p1 =(a+b+c)/2
s = p1*(p1-a)*(p1-b)*(p1-c)**0.5
print(p)
print(s)
