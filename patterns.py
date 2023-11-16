import math
radius = 5

for i in range(-radius, radius + 1):
    for j in range(-radius, radius + 1):
        if math.sqrt(i**2 + j**2) <= radius:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

width = 6
height = 4
for i in range(height):
    for j in range(width):
        print("*", end=" ")
    print()

height = 5
for i in range(1, height + 1):
    for j in range(i):
        print("*", end=" ")
    print()

height = 5
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print(" ")

