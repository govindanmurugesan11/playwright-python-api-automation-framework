"""
Topic: Regular Expressions (Regex)

Used for pattern matching.
"""

import re

text = "My email is govindan@test.com"

email = re.search(r"\S+@\S+\.\S+", text)

print(email.group())   # govindan@test.com

phone_text = "Call me on 9876543210"

number = re.search(r"\d{10}", phone_text)

print(number.group())  # 9876543210