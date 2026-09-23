"""
Topic: Anagram Checker

Two words are anagrams if they contain
the same letters in a different order.
"""

word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print("Anagram")          # Anagram
else:
    print("Not Anagram")