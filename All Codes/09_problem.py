#A) Count similar elements and print their index values

numbers = []

for i in range(20):
    value = int(input("Enter value: "))
    numbers.append(value)

element = int(input("Enter element to find: "))

print("Count:", numbers.count(element))
print("Index values:")

for i in range(20):
    if numbers[i] == element:
        print(i)

#B)Count even and odd values

numbers = []

for i in range(20):
    value = int(input("Enter value: "))
    numbers.append(value)

even = 0
odd = 0

for value in numbers:
    if value % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even values:", even)
print("Odd values:", odd)

#c)Count positive and negative values

numbers = []

for i in range(20):
    value = int(input("Enter value: "))
    numbers.append(value)

positive = 0
negative = 0

for value in numbers:
    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1

print("Positive values:", positive)
print("Negative values:", negative)
