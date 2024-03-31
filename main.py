p = 0
s = 0
halfp = 0
while True:
    a = int(input("Ввидите сторону A: "))
    b = int(input("Ввидите сторону B: "))
    c = int(input("Ввидите сторону C: "))
    if a+b>c and a+c>b and b+c>a:
        p =a+b+c
        print("Пиримите: ",p)
        halfp=p/2
        s =(halfp*(halfp-a)*(halfp-b)*(halfp-c))**0.5
        print("Площадь:",s)
        break
    else:
        print("Треугольник НЕ возможен! Попобуйте еще раз.")