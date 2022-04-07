# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('hirstspot.jpg', 30)
# rgb=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)
# print(rgb)
import turtle
import random
from turtle import Turtle,Screen
turtle.colormode(255)
tim=Turtle()
screen=Screen()
screen.screensize(10,10)
color_list=[(236, 234, 230), (238, 229, 234), (228, 238, 232), (227, 233, 240), (237, 40, 115), (142, 27, 70), (219, 162, 59), (238, 71, 36), (14, 144, 89), (182, 166, 43), (31, 126, 191), (54, 190, 229), (245, 221, 50), (179, 41, 96), (128, 190, 101), (78, 27, 81), (39, 172, 118), (250, 225, 1), (210, 61, 31), (214, 131, 167), (150, 29, 26), (24, 194, 220), (239, 163, 194), (163, 212, 174), (244, 167, 150), (7, 110, 54), (137, 212, 230), (53, 136, 204), (83, 28, 27), (156, 197, 231)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100
for count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if(count%10 == 0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen.exitonclick()