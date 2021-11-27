import turtle

pegasus=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("#994444")

pegasus.speed("fastest")

def star(size):
        
        if size<+10:
            return
        else: 
            pegasus.begin_fill()
            pegasus.fillcolor("green")
            for i in range(5):   
                
                pegasus.forward(size)
                star(size/3)
                pegasus.left(216)
            pegasus.end_fill()
        
pegasus.penup()
pegasus.goto((-200,100))
pegasus.pendown()      
star(180)   




screen.exitonclick()