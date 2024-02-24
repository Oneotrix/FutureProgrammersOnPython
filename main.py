number = int(input("Введите число: "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

if number < 0:
    print("Отрицательне число")
else:
    print("Факториал цисла", number, ":", factorial(number))