import turtle

# A function to draw a square shape given a specific length
# Enables you to create square shapes of different sizes
def draw_square(line_length):
    turtle.pendown()
    for _ in range(4):
        turtle.forward(line_length)
        turtle.left(90)

# Draw a square, specifying the length of a line (side of the square)
#draw_square(50)

# Uses the draw_square function but first changes the starting angle
# Caling this function repeadedly will create a tilted square pattern 
def draw_tilted_squared(line_length):
    for _ in range(3):
        turtle.left(20)
        draw_tilted_squared(100)

# draw_tilted_square(50)

def draw_hexagon(line_length):
    turtle.pendown()
    for _ in range(6):
        turtle.forward(line_length)
        turtle.left(60)

# Changing the pen color
turtle.pencolor("blue")

# Create 6 hexagons, moving to the bottom right corner to start a new one
for i in range(6):
    turtle.pensize(i+3)
    draw_hexagon(100)
    turtle.forward(100)
    turtle.right(60)


# Stop the Python Turtle window from disappearing until we click on the window with the mouse
turtle.exitonclick()
