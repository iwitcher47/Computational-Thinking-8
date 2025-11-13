# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)
s2 = create_sprite("Obi",0,300)
# Section 3: define movement controls
def move_up():
    s1.setheading(90)
    s1.forward(10)
        
def move_down():
    s1.setheading(270)
    s1.forward(10)
    
def move_left():
    s1.setheading(180)
    s1.forward(10)
    
def move_right():    
    s1.setheading(0)
    s1.forward(10)

def draw():
    s1.pendown()

def stopdraw():
    s1.penup()

def reset(x,y):
    s1.clear()
    s1.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(draw, "m")
window.onkeyrelease(stopdraw, "m")
window.onscreenclick(reset)
# Section 4: define other controls
# hide and show controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")





def move_up1():
    s2.setheading(90)
    s2.forward(10)
        
def move_down1():
    s2.setheading(270)
    s2.forward(10)
    
def move_left1():
    s2.setheading(180)
    s2.forward(10)
    
def move_right1():    
    s2.setheading(0)
    s2.forward(10)

def draw1():
    s2.pendown()

def stopdraw1():
    s2.penup()

window.onkeypress(move_up1, "w")
window.onkeypress(move_down1, "s")
window.onkeypress(move_left1, "a")
window.onkeypress(move_right1, "d")
window.onkeypress(draw1, "x")
window.onkeyrelease(stopdraw1, "x")


# Section 5: game loop
window.listen()
while True:
    time.sleep(0.1)
    window.update()