g = 0
h = 0

while True:
    print("введите число")
    a = int(input("Ответ:"))

    print("повторите ещё раз")
    b = int(input("Ответ:"))

    print("ещё")
    c = int(input("Ответ:"))

    print("ЕЩЁ!")
    i = int(input("Ответ"))

    print("загрузка...")

    g = a + i
    h = b + c

    if g == h:
        print("равно")
        break
    else:
        print("ошибка, повторите ещё раз")