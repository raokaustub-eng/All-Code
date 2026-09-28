numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for value in numbers:
    if value not in unique:
        unique.append(value)

print("Original list:", numbers)
print("List without duplicates:", unique)