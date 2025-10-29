def generate_series(a):
    """Generate odd number series based on input a."""
    n = a if a % 2 != 0 else a - 1
    series = [2 * i + 1 for i in range(n)]
    return series

a = int(input("Enter a number: "))
result = generate_series(a)
print(", ".join(map(str,result)))                                                                                                                                                                  