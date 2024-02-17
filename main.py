numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filterNumbers(numbers, operation):
    count = operation(numbers)
    total = sum(numbers)
    return [count, total]

result = filterNumbers(numbers, lambda x: len(x))

print(result)