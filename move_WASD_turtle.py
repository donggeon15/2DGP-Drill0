import turtle

def move_turtle_w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_turtle_d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def move_turtle_a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def move_turtle_s():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()


def reset_turtle():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(move_turtle_w,'w')
turtle.onkey(move_turtle_a,'a')
turtle.onkey(move_turtle_s,'s')
turtle.onkey(move_turtle_d,'d')
turtle.onkey(reset_turtle,'Escape')
turtle.listen()


