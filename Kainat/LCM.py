import math

# Function to find LCM of a list of numbers
def find_lcm(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = (result * num) // math.gcd(result, num)
    return result

# Example usage:
numbers = [12, 18, 24]  # Replace with the numbers for which you want to find the LCM
lcm = find_lcm(numbers)
print(f"The LCM of {numbers} is {lcm}")
