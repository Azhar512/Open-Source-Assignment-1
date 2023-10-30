import inflect

def number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number)
    return words

# Example usage:
num = 12345  # Replace with the number you want to convert to words
words = number_to_words(num)
print(f"{num} in words is: {words}")
