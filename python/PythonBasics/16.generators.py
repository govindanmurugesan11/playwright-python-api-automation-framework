"""
Topic: Generators
"""

def numbers():

    for i in range(1, 6):
        yield i

for number in numbers():
    print(number)

# 1
# 2
# 3
# 4
# 5