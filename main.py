numbers = [4, 2, 7, 1, 5, 3, 6, 8, 9, 10]

def sortNumbers(numbers, sorting):
    sorted_numbers = sorting(numbers)
    return sorted_numbers

sortedNumbers = sortNumbers(numbers, lambda x: sorted(x))

print(sortedNumbers)