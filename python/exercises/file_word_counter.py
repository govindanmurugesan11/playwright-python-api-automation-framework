"""
Topic: Count Words in a File
"""

with open("sample.txt", "w") as file:
    file.write("Python is easy to learn")

with open("sample.txt", "r") as file:
    text = file.read()

word_count = len(text.split())

print("Word Count:", word_count)
# Word Count: 5