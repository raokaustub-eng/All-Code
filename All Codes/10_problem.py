#A)Sort in ascending order using sorted()

numbers = []

for i in range(10):
    value = int(input("Enter value: "))
    numbers.append(value)

sorted_list = sorted(numbers)

print("Ascending order:", sorted_list)

#B)Sort in descending order using sort()

numbers = []

for i in range(10):
    value = int(input("Enter value: "))
    numbers.append(value)

numbers.sort(reverse=True)

print("Descending order:", numbers)

#c)Display length of list

numbers = []

for i in range(10):
    value = int(input("Enter value: "))
    numbers.append(value)

print("Length of list:", len(numbers))