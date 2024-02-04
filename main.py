import time

num1 = 1
num2 = 2.0
str = "num3"
num4 = True
print(num2)
print(num1)
print(str)
print(num4)



name = "Костя"
print("Мое имя:",name)
f = 0
while True:
    print("Ваше имя???")
    f =input()
    if f != 0:
        break
print("Ваше имя:",f)
time.sleep(3)
print("Тупое имя",f,",не то что Костя")
time.sleep(3)
print("боже я рофлю",f,"нормальное имя")
time.sleep(1)
#while True:
#    l = input()
#    print("Ожидаю команды...")
