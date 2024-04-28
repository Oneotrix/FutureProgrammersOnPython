sum = 1
while True:
    try:
        for i in range(1,6):
        data = int(input(f"введите данные:"))
        sum *= data
        break
    except:
        sum = 0
        print("введите повторно:")

    print(sum)