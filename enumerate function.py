fruits = ['apple', 'banana', 'orange', 'grape']

# Using enumerate to iterate through a list along with its index
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print()

# Using start parameter to customize the starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")
