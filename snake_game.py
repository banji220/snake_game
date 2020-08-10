import turtle
import time
import random
# Set up the screen

windows = turtle.Screen()
windows.title("Snake Game by Banji")
windows.bgcolor("Pink")
windows.setup(width = 800, height = 800)
windows.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food

food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("green")
food.penup()
food.goto(0, 100)

# Segments List
segments = []



# Go Functions
def go_up():
    if head.direction != "Down":
        head.direction = "Up"
 
def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"  

def go_right():
    if head.direction != "Left":
        head.direction = "Right"
    
    
# Move-Up Function
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
windows.onkeypress(go_up, "w")
windows.onkeypress(go_down, "s")
windows.onkeypress(go_left, "a")
windows.onkeypress(go_right, "d")


      
# Main Game Loop

while True:
    windows.update()
    
    #Check for  a collision with the border
    if head.xcor() > 397 or head.xcor() < -397 or head.ycor() > 397 or head.ycor() < -397:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
    
    #Check for conflicting food and head!
    if head.distance(food) < 20:
        # Move the food to a random place
        x = random.randint(-390, 390)
        y= random.randint(-390, 390)
        food.goto(x, y)
        
        
        # Add a segment
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
    #Move the end segment first in reverse order
    for item in range(len(segments)-1, 0, -1):
        x = segments[item-1].xcor()
        y = segments[item-1].ycor()
        segments[item].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    # Check for head collision with the body segments
    for segment in segments:
        # print(segment.distance(head))
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segmnet in segments:
                segment.goto(1000, 1000)
            segment.clear()
            # segment.clear()
    time.sleep(0.03)
windows.mainloop()

# Need to find a solution to improve the speed after touching its own body, it takes around 3 or 4 seconds or mor
#to reset the game, so it could be boring for players.(Need to fix this bug)