def right_triangle(a, b, c):
    if a*a + b*b == c*c:
        return True
    elif a*a + c*c == b*b:
        return True
    elif b*b + c*c == a*a:
        return True
    else:
        return False


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if right_triangle(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
