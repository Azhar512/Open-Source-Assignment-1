def count_words(input_string):
    words = input_string.split()
    return len(words)

# Example usage:
text = "This is a sample sentence with some words."  # Replace with the text you want to count words in
word_count = count_words(text)
print(f"The number of words in the text is: {word_count}")
