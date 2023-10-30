import math

# Function to find GCD of a list of numbers
def find_gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

# Example usage:
numbers = [12, 18, 24]  # Replace with the numbers for which you want to find the GCD
gcd = find_gcd(numbers)
print(f"The GCD of {numbers} is {gcd}")
