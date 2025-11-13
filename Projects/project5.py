# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, pygame, random
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

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()



window = turtle.Screen()
window.tracer(0)


set_background("macpaint3")
s1 = create_sprite("macpaintbrush",100,0)
brushbutton = create_sprite("Macpaintbrushbuttondown")
cat = create_sprite("cat",-300,250)
cat2 = create_sprite("cat2",-230,250)

s1.penup()

def spriteMotion(event):
    x, y = event.x, event.y
    s1.goto(x-359, -y+285)

canvas = turtle.getcanvas()
canvas.bind('<Motion>', spriteMotion)
drawingtime = 0

drawing = 0

s1.pensize(2)

def draw():
	s1.pendown()

def stopdraw():
    s1.penup()

def clear():
    s1.clear()

def drawornot(x,y):
	global drawing
	if drawing == 0:
		draw()
		drawing = 1
	else:
		stopdraw()
		drawing = 0

def buttonordraw(x,y):
	print((x,y))
	if x > -334 and x < -314 and y > 82 and y < 102:
		s1.pensize(20)
		#print("brush")
	elif x > -300 and x < -280 and y > 82 and y < 102:
		s1.pensize(2)
		#print("pencil")
	elif x > -334 and x < -314 and y > 114 and y < 140:
		s1.penup()
		clear()
	else:
		#print("drawornot")
		drawornot(x,y)

window.onkeypress(clear, "c")
window.onscreenclick(buttonordraw)

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.01)
	timer += 1  
	
	cat.forward(.1)
	cat2.forward(.1)





	window.update()

	# if :
	# 	break
	

print("Game Over")