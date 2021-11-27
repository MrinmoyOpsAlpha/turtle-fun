import turtle
a=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')

col=('white','red','orange','yellow','green','blue','cyan')
a.speed("fastest")
a.hideturtle()

for i in range (100):
    a.dot(10)

    a.forward(i*4)
    a.left(91)
    a.color(col[i%7])


screen.exitonclick()
