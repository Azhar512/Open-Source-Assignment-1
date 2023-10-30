def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Example usage:
n = 10  # Replace with the number of Fibonacci numbers you want to generate
fib_sequence = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fib_sequence}")
