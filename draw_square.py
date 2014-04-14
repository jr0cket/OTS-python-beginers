import turtle

# A function to draw a square shape given a specific length
# Enables you to create square shapes of different sizes
def draw_square(line_length):
    turtle.pendown()
    for _ in range(4):
        turtle.forward(line_length)
        turtle.left(90)

# Draw a square, specifying the length of a line (side of the square)
draw_square(50)

# Stop the Python Turtle window from disappearing until we click on the window with the mouse
turtle.exitonclick()
