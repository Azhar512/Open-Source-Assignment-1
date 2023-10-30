def factorize_number(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors

# Example usage:
number = 60  # Replace with the number you want to factorize
factors = factorize_number(number)
print(f"The prime factors of {number} are: {factors}")
