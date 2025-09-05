from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


timmy.shape("turtle")


screen.setup (width=800, height=800, startx=0, starty=0)

def move_forwards():
    timmy.forward(5)
screen.listen()
while True:
    screen.onkey(key="UP", fun=move_forwards)
    screen.exitonclick()




