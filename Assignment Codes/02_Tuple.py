
t = (10, 20, 30, 40)

print("Original Tuple:", t)


print("First element:", t[0])


t = t + (50,)
print("After adding:", t)


temp = list(t)
temp.remove(30)
t = tuple(temp)

print("After removing:", t)


print("Length:", len(t))


print("Count of 20:", t.count(20))