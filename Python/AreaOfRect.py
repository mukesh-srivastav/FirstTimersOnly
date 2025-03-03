def areaOfRect(l, w):
    return l * w

print("Welcome to my program to find the area of a rectangle")
length = int(input("Enter Length of Rectangle: "))
width = int(input("Enter Width of Rectangle: "))
print("Area of Rectangle = ",areaOfRect(length, width))