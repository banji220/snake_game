import turtle
import time


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
head.goto(0, 0)
head.direction = "stop"



# Go Functions
def go_up():
    head.direction = "Up"
 
def go_down():
    head.direction = "Down"

def go_left():
    head.direction = "Left"  

def go_right():
    head.direction = "Right"
    
def move():
    # Move Up 
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 10)
        
    # Move Down 
    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 10)
    
    # Move Left 
    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 10)
    
    # Move Right 
    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 10)
        
# Keyboard Binding
windows.listen()
windows.onkeypress(go_up, key = "w")
windows.onkeypress(go_down, key = "s")
windows.onkeypress(go_left, key = "a")
windows.onkeypress(go_right, key = "d")
# Main Game Loop
while True:
    windows.update()
     
    move()
    time.sleep(0.1)
windows.mainloop()


