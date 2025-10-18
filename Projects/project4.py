##################################################
########DONT MESS WITH############################
import turtle
t = turtle.Turtle()

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
###############################################
###############################################

t.goto(-80,-100)
t.color("pink")
t.speed(10)

###########################
####the bg################
t.screen.bgcolor("black")


####################################
#########josh's head################
ct8 = create_sprite("josh", -35, 0)

#####################################
##########the Pattern itself#########
for i in range(100):
    t.color("magenta")
    t.forward(100+i)
    t.left(50)
    t.color("cyan")
    t.forward(100+i)
    t.left(50)
    t.color("orange")
    t.forward(100+i)
    t.left(50)

################################################
##############the words that say CT8############
m1 = create_sprite("alien", -150, -250)
m1.color("lightblue")
m1.write("CT8",font = ("Arial", 100, "normal"))
m1.hideturtle()

turtle.exitonclick()

