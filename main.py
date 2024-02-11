import time

num1 = 4
num2 = 12
out = num1 + num2
print("4+12 =",out)
out = num1 - num2
print("4-12 =",out)
out = num1 * num2
print("4*12 =",out)
out = num2 / num1
print("12/4 =",out)
out = num1 ** num2
print("4**12 =",out)
out = num1 % num2
print("4%12 =",out)
out = num1 // num2
print("4//12 =",out)




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
