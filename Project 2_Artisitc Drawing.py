import turtle

# Set up my turtle window
wn = turtle.Screen()
wn.bgcolor("skyblue")

# Set up the turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)

# Draw the landscape_grass
my_turtle.penup()
my_turtle.goto(-400, -100)
my_turtle.pendown()
my_turtle.color("limegreen")
my_turtle.begin_fill()
for _ in range(2):
    my_turtle.forward(800)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()



# Draw the left side of the mountain
my_turtle.penup()
my_turtle.goto(-400, -100)
my_turtle.pendown()
my_turtle.color("slategrey")
my_turtle.begin_fill()
for _ in range(3):
    my_turtle.forward(300)
    my_turtle.left(120)
my_turtle.end_fill()

# Draw the right side of the mountain
my_turtle.penup()
my_turtle.goto(100, -100)
my_turtle.pendown()
my_turtle.begin_fill()
for _ in range(3):
    my_turtle.forward(300)
    my_turtle.left(120)
my_turtle.end_fill()

# Draw the middle mountain
my_turtle.penup()
my_turtle.goto(-160, -100)
my_turtle.pendown()
my_turtle.color("slategrey")
my_turtle.begin_fill()
for _ in range(3):
    my_turtle.forward(400)
    my_turtle.left(120)
my_turtle.end_fill()

# Draw the snow ontop of the mountains, middle
my_turtle.penup()
my_turtle.goto(-35, 120)
my_turtle.pendown()
my_turtle.color("floralwhite")
my_turtle.begin_fill()
my_turtle.left(35)
my_turtle.forward(60)
my_turtle.right(90)
my_turtle.forward(30)
my_turtle.left(100)
my_turtle.forward(45)
my_turtle.right(85)
my_turtle.forward(65)
my_turtle.left(160)
my_turtle.forward(150)
my_turtle.end_fill()

# snow for left mountain top
my_turtle.penup()
my_turtle.goto(-215, 100)
my_turtle.pendown()
my_turtle.color("floralwhite")
my_turtle.begin_fill()
my_turtle.forward(70)
my_turtle.left(120)
my_turtle.forward(75)
my_turtle.left(150)
my_turtle.forward(45)
my_turtle.right(90)
my_turtle.forward(45)
my_turtle.left(120)
my_turtle.end_fill()

# snow for right mountain top
my_turtle.penup()
my_turtle.goto(203, 80)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.forward(95)
my_turtle.right(120)
my_turtle.forward(80)
my_turtle.right(150)
my_turtle.forward(50)
my_turtle.left(70)
my_turtle.end_fill()

my_turtle.left(50)

# draw a sun 
my_turtle.penup()
my_turtle.goto(-500, 350)
my_turtle.pendown()
my_turtle.color("yellow")
my_turtle.begin_fill()
my_turtle.circle(125)
my_turtle.end_fill()

# draw multiple trees on the landcape
def tree():
    # Tree stem
    my_turtle.color("peru")
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(40)
        my_turtle.left(90)
        my_turtle.forward(10)
        my_turtle.left(90)
    my_turtle.end_fill()

    # Turn the turtle around
    my_turtle.forward(10)
    my_turtle.left(90)
    my_turtle.forward(5)

    # The bush/leaves on trees
    my_turtle.color("darkgreen")
    my_turtle.begin_fill()
    my_turtle.circle(25)
    my_turtle.end_fill()

    my_turtle.right(90)

# Define a list of tree positions (x, y)
tree_positions = [(-25, -200), (200, -150), (300, -250), (-300, -250), (-200, -100)]

# Use a for loop to draw the trees at the specified positions
for position in tree_positions:
    x, y = position
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    tree()


# Hide the turtle
my_turtle.hideturtle()

# Close the drawing window on click
wn.exitonclick()
