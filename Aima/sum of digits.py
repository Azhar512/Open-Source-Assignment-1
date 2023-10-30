def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

# Example usage:
num = 12345  # Replace with the number for which you want to find the sum of digits
result = sum_of_digits(num)
print(f"The sum of the digits in {num} is {result}")
