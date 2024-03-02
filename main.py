def calculateSumOfRange(start, end):
    sum = 0
    for i in range(start, end):
        sum += i
    print("sum:", sum)

calculateSumOfRange(100, 501)