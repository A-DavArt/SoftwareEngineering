def get_duplicates(numbers):
    duplicates = []
    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    return duplicates

print(get_duplicates([1, 2, 3, 4, 5]))
print(get_duplicates([1, 2, 3, 2, 4, 1, 5, 6, 7, 8, 9, 7]))
print(get_duplicates([10, 20, 30, 40, 50, 10, 20, 30]))
