people = [
    {"name": "Alice", "age": 30, "city": "Bucharest"},
    {"name": "Bob", "age": 25, "city": "Cluj"},
    {"name": "Charlie", "age": 25, "city": "Bucharest"},
    {"name": "Diana", "age": 35, "city": "Cluj"},
]

# Sort by age → city → name
sorted_people = sorted(people, key=lambda p: (p["age"], p["city"], p["name"]))

for person in sorted_people:
    print(person)