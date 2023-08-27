import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
colors_list = [(246, 240, 244), (235, 241, 246), (1, 13, 31), (219, 127, 106), (242, 214, 69), (150, 84, 39), (215, 87, 64),
               (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19),
               (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (145, 227, 216),
               (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]
#(52, 25, 17), (9, 105, 160) , (0, 63, 145), (10, 97, 58), (122, 193, 148), (8, 140, 85), (207, 74, 104)
tim = Turtle()
screen = Screen()
tim.speed("fastest")

num_y =0
for k in range (10):
    tim.penup()
    tim.hideturtle()
    tim.goto(-250, -250+num_y)
    num_y += 50
    for i in range(10):
        tim.pendown()
        tim.dot(20,random.choice(colors_list))
        tim.penup()
        tim.fd(50)




screen.exitonclick()