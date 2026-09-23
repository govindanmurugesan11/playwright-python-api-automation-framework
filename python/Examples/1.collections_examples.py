"""
Topic: Collections Module

Provides specialised container data types.
"""

from collections import Counter

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

fruit_count = Counter(fruits)

print(fruit_count)
# Counter({'apple': 3, 'banana': 2, 'orange': 1})

print(fruit_count["apple"])  # 3

print(fruit_count["banana"])  # 2