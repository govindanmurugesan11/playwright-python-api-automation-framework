"""
Topic: Palindrome Checker

A palindrome reads the same forward and backward.
"""

word = "madam"

if word == word[::-1]:
    print("Palindrome")       # Palindrome
else:
    print("Not a Palindrome")

    #Alternative

word = "python"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")  # Not a Palindrome