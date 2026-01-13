# generate_cities.py

data = [
    ("Agadir", 13),
    ("Ben Guerir", 28.5),
    ("Rabat", 14.5),
    ("CasaBlanca", 19),
]

# Print to stdout
for city, value in data:
    print(f"{city};{value}")

with open("wheater.txt", "w", encoding="utf-8") as f:
    for city, value in data:
        f.write(f"{city};{value}\n")

