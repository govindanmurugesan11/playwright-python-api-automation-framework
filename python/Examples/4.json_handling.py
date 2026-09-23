"""
Topic: JSON Handling

Used heavily in API Automation.
"""

import json

employee = {
    "name": "Govindan",
    "role": "QA Engineer",
    "experience": 15
}

json_data = json.dumps(employee)

print(json_data)
# {"name": "Govindan", "role": "QA Engineer", "experience": 15}

python_object = json.loads(json_data)

print(python_object["name"])  # Govindan

print(python_object["role"])  # QA Engineer