"""
Topic: List Comprehensions
"""

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)
# [1, 4, 9, 16, 25]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
# [2, 4]