student = {
    "name": "Kaustub",
    "age": 18,
    "marks": 85
}

print("Original Dictionary:", student)


student["city"] = "Pune"
print("After adding:", student)

student["marks"] = 90
print("After updating:", student)


student.pop("age")
print("After removing:", student)


print("Keys:", student.keys())


print("Values:", student.values())