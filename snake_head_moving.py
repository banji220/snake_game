import turtle



# Set up the screen
windows = turtle.Screen()
windows.title("Snake Game by Banji")
windows.bgcolor("Pink")
windows.setup(width = 1000, height = 700)
windows.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
# head.goto(0, 0)
head.direction = "Up"


def move():
    # Move Up 
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 10)

# Main Game Loop
while True:
    windows.update()
     
    move()

windows.mainloop()


