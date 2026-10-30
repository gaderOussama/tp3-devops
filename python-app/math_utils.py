def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    return 1 if n <= 1 else n * factorial(n - 1)
