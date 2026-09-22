"""
Topic: Dictionaries
"""

employee = {
    "name": "Govindan",
    "role": "QA Engineer",
    "experience": 15
}

print(employee["name"])           # Govindan

employee["location"] = "Stockholm"

print(employee)
# {'name': 'Govindan', 'role': 'QA Engineer',
#  'experience': 15, 'location': 'Stockholm'}

print(employee.keys())
# dict_keys(['name', 'role', 'experience', 'location'])