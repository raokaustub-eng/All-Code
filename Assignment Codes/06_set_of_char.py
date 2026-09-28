import re

s = input("Enter a string: ")

if re.fullmatch("[a-zA-Z0-9]+", s):
    print("String contains only allowed characters.")
else:
    print("String contains other characters.")