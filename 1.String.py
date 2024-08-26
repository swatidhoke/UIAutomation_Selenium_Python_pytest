# Commonly Used String Functions in Python:
# 1. len() - Returns the length of the string.
#    Example: len("hello") returns 5.
#
# 2. str.upper() - Converts all characters in the string to uppercase.
#    Example: "hello".upper() returns "HELLO".
#
# 3. str.lower() - Converts all characters in the string to lowercase.
#    Example: "HELLO".lower() returns "hello".
#
# 4. str.strip() - Removes leading and trailing whitespace from the string.
#    Example: "  hello  ".strip() returns "hello".
#
# 5. str.replace(old, new) - Replaces occurrences of a substring with a new substring.
#    Example: "hello world".replace("world", "Python") returns "hello Python".
#
# 6. str.split(separator) - Splits the string into a list of substrings based on the separator.
#    Example: "hello world".split(" ") returns ["hello", "world"].
#
# 7. str.join(iterable) - Joins elements of an iterable into a single string with a separator.
#    Example: ", ".join(["apple", "banana", "cherry"]) returns "apple, banana, cherry".
#
# 8. str.find(substring) - Finds the index of the first occurrence of a substring. Returns -1 if not found.
#    Example: "hello world".find("world") returns 6.
#
# 9. str.startswith(prefix) - Checks if the string starts with the specified prefix.
#    Example: "hello world".startswith("hello") returns True.
#
# 10. str.endswith(suffix) - Checks if the string ends with the specified suffix.
#     Example: "hello world".endswith("world") returns True.

# 1. Check if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]
# Example usage:
s = "racecar"
print("Programme is_palindrome",is_palindrome(s))  # Output: True


# 2. Count the Number of Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0  # Changed variable name from `sum` to `vowel_count`
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count
# Example usage:
s = "Hello World"
print("Programme count_vowels:",count_vowels(s))  # Output: 3


# 3. Find the Most Frequent Character in a String
def most_frequent_char(s):
    max_count = 0
    most_frequent = ''
    for char in s:
        count = s.count(char)
        # Optional: Remove the debug print statement
        # print(count)
        if count > max_count:
            max_count = count
            most_frequent = char
    return most_frequent
s = "hello"
print("Programme most_frequent_char:",most_frequent_char(s))


#4. Remove Duplicates from a String
#This program removes duplicate characters from a string while preserving the original order of characters.
def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
# Example usage:
s = "banana"
print("Programme remove_duplicates:" ,remove_duplicates(s))  # Output: "ban"
