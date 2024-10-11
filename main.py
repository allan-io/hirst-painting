import colorgram
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.speed("fastest")
color_palate = colorgram.extract('hirst.jpg', 20)

color_list = []
for color in color_palate:
    color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
    color_list.append(color_tuple)

print(color_list)

rgb_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

timmy.setpos(-150, -100)
y_coord = (-150)

for _ in range(10):
    timmy.setpos(-150, y_coord)

    timmy.dot(20, random.choice(rgb_list))
    timmy.forward(50)
    y_coord += 50
    for _ in range(9):
        timmy.dot(20, random.choice(rgb_list))
        timmy.forward(50)

timmy.hideturtle()
screen.exitonclick()