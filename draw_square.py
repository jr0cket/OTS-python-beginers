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

# Start the turtle higher up in the screen, so the hexagons pattern fits.
def initialise_turtle():
    turtle.penup()
    turtle.setx(-50)
    turtle.sety(100)
    turtle.pendown()

initialise_turtle()


# Create 6 hexagons, moving to the bottom right corner to start a new one
for i in range(6):
    turtle.pensize(i+3)
    # Change the color of the pen before drawing each hexagon
    for colorname in "Red", "Yellow", "Green", "Blue", "Orange", "Purple":
        turtle.pencolor(colorname)
        draw_hexagon(100)
        turtle.forward(100)
        turtle.right(60)

# My loops are not quite right as the above draws 6 different coloured hexagons 6 times over at the different thickness levels

# Stop the Python Turtle window from disappearing until we click on the window with the mouse
turtle.exitonclick()
