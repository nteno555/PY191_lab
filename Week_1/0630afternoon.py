import random

iterations = 1000000
circle_points = 0
square_points = 0

while (iterations > 0):
    x = (random.random() - 0.5) * 2.0
    y = (random.random() - 0.5) * 2.0

    if (x*x + y*y <= 1.0):
        circle_points += 1
    square_points += 1
    iterations -= 1

print(f"π is approximately {4 * (circle_points/square_points)}")