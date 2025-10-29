def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        count = sum(1 for n in numbers if n % i == 0)
        result[i] = count
    return result

numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(numbers))