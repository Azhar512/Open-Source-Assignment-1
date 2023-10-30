def count_vowels_and_consonants(text):
    text = text.lower()  # Convert the text to lowercase for case insensitivity
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count

# Example usage:
input_text = "Hello, World!"  # Replace with the text you want to analyze
vowels, consonants = count_vowels_and_consonants(input_text)

print(f"Text: {input_text}")
print(f"Vowel Count: {vowels}")
print(f"Consonant Count: {consonants}")
