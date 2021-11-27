# import colorgram

# colors=colorgram.extract("images.jpg",30)
# rgb_colors=[]

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
 
# print(rgb_colors)

import random
import turtle

tuk=turtle.Turtle()
turtle.colormode(255)
tuk.speed("fastest")

colors=[ (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]
tuk.setheading(225)
tuk.penup()
tuk.hideturtle()
tuk.forward(300)
tuk.setheading(0)

no_of_dots=100
for i in range(1,no_of_dots+1):
    tuk.dot(10,random.choice(colors))
    tuk.forward(50)    
    if i %10 == 0:
        tuk.setheading(90)
        tuk.forward(50)
        tuk.setheading(180)
        tuk.forward(500)
        tuk.setheading(0)



screen=turtle.Screen()
screen.exitonclick()