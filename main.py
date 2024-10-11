import colorgram
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
color_palate = colorgram.extract('hirst.jpg', 10)

color_list = []
for color in color_palate:
    color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
    color_list.append(color_tuple)

print(color_list)

rgb_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85)]


# dot 50space 100 * 10
for _ in range(10):
    timmy.dot(20, random.choice(rgb_list))
    timmy.forward(50)

screen.exitonclick()



