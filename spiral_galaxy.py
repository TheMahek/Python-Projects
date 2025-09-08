from turtle import *
import colorsys
import random

# Setup screen
setup(800, 800)         # Set window size
bgcolor("black")        # Background color
tracer(3)               # Speed up drawing
pensize(2)              # Pen thickness

# Draw random stars in background
penup()
for _ in range(100): 
    x = random.randint(-380, 380)   # Random X position
    y = random.randint(-380, 380)   # Random Y position
    pencolor("white")               # Star color
    goto(x, y)
    dot(random.randint(2, 5))       # Star size
pendown()

# Move spiral starting point
penup()
goto(0, 180)  
pendown()

# Draw colorful spiral
spiral_size = 150
h = 0.7
for i in range(spiral_size):   
    c = colorsys.hsv_to_rgb(h, 1, 1)   # Generate rainbow color
    color(c)
    h += 0.004
    circle(spiral_size - i, 90)        # First arc
    lt(90)
    lt(20)
    circle(spiral_size - i, 90)        # Second arc
    lt(18)

done()


# Add spiral galaxy with stars