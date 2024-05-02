def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Get user input for base and height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))


# Calculate the area
area = calculate_triangle_area(base, height)

# Print the result
print("The area of the triangle is:", area)
