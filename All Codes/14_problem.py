numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)


value = int(input("Enter value to insert: "))
index = int(input("Enter index: "))

numbers.insert(index, value)

print("After insertion:", numbers)


index = int(input("Enter index to delete: "))

numbers.pop(index)

print("After deletion:", numbers)

# Display
print("Final list:", numbers)