N = int(input("Enter the number of integers: "))

numbers = []
for i in range(N):
    num = int(input("Enter an integer: "))
    numbers.append(num)

countOfZeros = numbers.count(0)

print("Number of zeros:", countOfZeros)