from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
colors = ["red","orange","yellow","green","blue","indigo","purple"]


def draw_shape(sides, colors):
	for _ in range(sides):
		timmy.forward(100)
		angle = 360 / sides
		timmy.right(angle)
	timmy.color(choice(colors))


for i in range(3, 15):
	draw_shape(i, colors)



screen = Screen()
screen.delay(0)
screen.exitonclick()
