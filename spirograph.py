import turtle
import random
tom=turtle.Turtle()
a=turtle.Turtle()
turtle.colormode(255)
screen=turtle.Screen()
screen.bgcolor('black')



def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    new_color=(r,g,b)
    return new_color

def hexo(gap_size):
    for i in range(360//gap_size):
        tom.speed("fastest")
        tom.color(random_color())   
        tom.setheading(tom.heading() + gap_size)
        tom.circle(40)



hexo(18)

col=('white','red','orange','yellow','green','blue','cyan')
a.speed("fastest")
a.hideturtle()

for i in range (500):
    a.dot(10)
    a.penup()
    a.forward(i*4)
    a.left(92)
    a.color(col[i%7])    


screen.exitonclick()