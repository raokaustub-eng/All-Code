list1 = []
list2 = []

n1 = int(input("Enter number of elements in list 1: "))

for i in range(n1):
    value = int(input("Enter value: "))
    list1.append(value)

n2 = int(input("Enter number of elements in list 2: "))

for i in range(n2):
    value = int(input("Enter value: "))
    list2.append(value)

merged_list = list1 + list2

print("Merged list:", merged_list)