import math
# Input coordinates of the three points
print("Enter the coordinates of point 1 (x1 y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Enter the coordinates of point 2 (x2 y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

print("Enter the coordinates of point 3 (x3 y3):")
x3 = float(input("x3: "))
y3 = float(input("y3: "))

# Check if the points are collinear using the area formula
# If the area of the triangle is zero, the points are collinear
area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

if area == 0:
    print("The points are collinear and do not form a triangle.")
else:
    # Calculate the squared lengths of the sides of the triangle
    side1_sq = math.floor(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))  # Length between point 1 and point 2
    side2_sq = math.floor(math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)) # Length between point 2 and point 3
    side3_sq = math.floor(math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)) # Length between point 3 and point 1
    #printing the edges
    print("Length between point 1 and point 2:",side1_sq)
    print("Length between point 2 and point 3:",side2_sq)
    print("Length between point 3 and point 1:",side3_sq)
    print("point 1 and 2:",side1_sq)
    print("point 2 and 3:",side2_sq)
    print("point 3 and 1:",side3_sq)
    

    # Determine the type of triangle
    if side1_sq == side2_sq == side3_sq:
        print("The points form an Equilateral triangle.")
    elif side1_sq == side2_sq or side2_sq == side3_sq or side3_sq == side1_sq:
        print("The points form an Isosceles triangle.")
    else:
        print("The points form a Scalene triangle.")
