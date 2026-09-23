"""
Topic: Datetime Module

Used for handling dates and times.
"""

from datetime import datetime

current_time = datetime.now()

print(current_time.year)   # Example: 2026
print(current_time.month)  # Example: 9
print(current_time.day)    # Example: 22

formatted_date = current_time.strftime("%d-%m-%Y")

print(formatted_date)      # Example: 22-09-2026