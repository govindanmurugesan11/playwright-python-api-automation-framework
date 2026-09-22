"""
Topic: Exception Handling
"""

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")     # Cannot divide by zero

finally:
    print("Execution completed")       # Execution completed