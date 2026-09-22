"""
Topic: Lists
"""

cars = ["Volvo", "BMW", "Tesla"]

cars.append("Audi")

print(cars)
# ['Volvo', 'BMW', 'Tesla', 'Audi']

print(cars[0])                    # Volvo

print(len(cars))                  # 4

cars.remove("BMW")

print(cars)
# ['Volvo', 'Tesla', 'Audi']