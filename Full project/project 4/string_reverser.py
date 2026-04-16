def reverse_string(text):
    return text[::-1]

def count_vowels_consonants(text):
    text = text.lower()
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

def is_palindrome(text):
    # Clean the string: lowercase and remove non-alphanumeric characters
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

# Main execution
phrase = input("Enter a phrase: ")

reversed_phrase = reverse_string(phrase)
print(f"Reversed phrase: {reversed_phrase}")

v_count, c_count = count_vowels_consonants(phrase)
print(f"Vowels: {v_count}, Consonants: {c_count}")

print(f"Is it a palindrome? {is_palindrome(phrase)}")
