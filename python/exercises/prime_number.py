"""
Topic: Prime Number Checker

A prime number is divisible only by
1 and itself.
"""

number = 17

is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime Number")       # Prime Number
else:
    print("Not a Prime Number")

    #Alternative

    number = 12

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")  # Not a Prime Number