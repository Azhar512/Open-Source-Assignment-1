def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

# Example usage:
num = 10  # Replace with the number you want to check
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
