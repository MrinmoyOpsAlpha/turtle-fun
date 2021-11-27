import turtle
t=turtle.Turtle()

screen=turtle.Screen()
screen.bgcolor("black")


t.speed("fastest")

a=0
b=0
t.penup()
t.goto((-600,80))
t.pendown()
while 1:
  
    t.pencolor("yellow")
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==210:
        break
    t.hideturtle()
   
    

t.penup()
t.goto((500,120))
t.pendown()
c=0
d=0
while 1:
    
    t.pencolor("red")
    t.forward(c)
    t.right(d)
    c+=3
    d+=1
    if d==210:
        break
    t.hideturtle()


t.penup()
t.goto((-130,200))
t.pendown()
e=0
f=0
while 1:
    
    t.pencolor("green")
    t.forward(e)
    t.right(f)
    e+=3
    f+=1
    if f==210:
        break
    t.hideturtle()


screen.exitonclick()