"""
Topic: Fibonacci Series

Each number is the sum of the previous two.
"""

n = 10

a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34