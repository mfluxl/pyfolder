import math # the pi import

# PART 1 

square_side = float(input("What is the length of a side of the square?"))
squarearea = square_side * square_side
print(squarearea)


length = float(input('What is the length of the rectangle?'))
width = float(input('What is the width of the rectangle?'))
rectanglearea = length * width
print(rectanglearea)

radius = float(input('What is the radius of the circle?'))
circlearea = radius * math.pi       #the math.pi function instead of 3.14
print(circlearea)

# PART 2 - single length value:

singlelength = float(input("what is the length?" ))

area_square = singlelength * singlelength
area_circle = singlelength * math.pi
volume_cube = singlelength**3
volume_sphere = 4/3 * math.pi * (singlelength**3)


print(f"The area of the square is {area_square:.1f}")
print(f"The area of the circle is {area_circle:.1f}")
print(f"The volume of the cube is {volume_cube:.1f}")
print(f"The volume of the sphere is {volume_sphere:.1f}")

#PART 3 - Centimeters version:

square_side_cm = float(input("What is the length of a side of the square in cm?"))
squarearea_cm = square_side_cm * square_side_cm
print(f"{squarearea_cm:.1f}cm²")
print(f"{squarearea_cm/10000:.1f}m²")

length_cm = float(input('What is the length of the rectangle in cm?'))
width_cm = float(input('What is the width of the rectangle in cm?'))
rectanglearea_cm = length_cm * width_cm
print(f"{rectanglearea_cm:.1f}cm²")
print(f"{rectanglearea_cm/10000:.1f}m²")

radius_cm = float(input('What is the radius of the circle?'))
circlearea_cm = radius_cm * math.pi       #the math.pi function instead of 3.14
print(f"{circlearea_cm:.1f}cm²")
print(f"{10000*circlearea_cm:.1f}m²")



