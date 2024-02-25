print( "Координаты центр квадрата,")
x0 = int(input("х:"))
y0 = int(input("y:"))
a = int(input("Длинна стороны квадрата:"))
print( "Координаты точки А,")
x = int(input("х:"))
y = int(input("y:"))
af = x0+a/2
bf = x0-a/2
afy = y0+a/2
bfy = y0-a/2
if bf<=x<=af:
    if bfy <= y <= afy:
        print("х принадлежит!")
    else:
        print("х не принадлежит!")
else:
    print("х не принадлежит!")