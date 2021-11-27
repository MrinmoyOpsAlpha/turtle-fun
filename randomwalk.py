
import turtle
import random
c=1
tom=turtle.Turtle()
turtle.colormode(255)

def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    k=(r,g,b)
    return k

directions=[0,90,180,270]

for _ in range(100):
   x=randomcolor()
   tom.color(x)
   tom.pensize(5)
   tom.speed("fastest")
   tom.forward(20)
   tom.setheading(random.choice(directions))
   
   


   
screen=turtle.Screen()
screen.exitonclick()
