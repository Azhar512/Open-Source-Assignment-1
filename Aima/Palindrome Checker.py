def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case insensitivity
    s = ''.join(e for e in s if e.isalnum())  # Remove non-alphanumeric characters
    return s == s[::-1]

# Example usage:
text = "A man, a plan, a canal, Panama"  # Replace with the text you want to check
if is_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
