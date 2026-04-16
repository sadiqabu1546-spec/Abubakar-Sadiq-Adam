# 1. Creation & Immutability
coordinates = (10.5, 20.2)
rgb_color = (255, 0, 0) # Red

print(f"Coordinates: {coordinates}")

# Attempting to modify (This will trigger a TypeError)
try:
    coordinates[0] = 15.0
except TypeError as e:
    print(f"Immutability Check: {e}")

# 2. Multiple Returns & Unpacking
def get_dimensions():
    length = 100
    width = 50
    return length, width  # Returns a tuple automatically

# Unpacking the returned tuple into separate variables
l, w = get_dimensions()
print(f"Unpacked Dimensions: Length = {l}, Width = {w}")

# 3. Tuples in Lists (City Data)
cities = [
    ("Abuja", 5000000),
    ("Kaduna", 1000000),
    ("Kano", 10000000)
]

print("\nCity Population List:")
for name, population in cities:
    print(f"- {name} has a population of {population:,}")
