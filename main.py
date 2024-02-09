firstNum = int(input())
secondNum = int(input())
def primeNum(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeRange(firstNum, secondNum):
    primeNumbers = []
    for num in range(firstNum, secondNum + 1):
        if primeNum(num):
            primeNumbers.append(num)
    return primeNumbers

primeNumbers = primeRange(firstNum, secondNum)
print(primeNumbers)

