import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()  

states = pd.read_csv("50_states.csv")
df = pd.DataFrame(states)
df_indexed = df.set_index('state')

states_left = len(df)
states_guessed = []
while states_left > 0:
    answer_state = screen.textinput(title=f"Guess the State! {states_left} left", prompt = "What's another State's name?").title()
    if answer_state in df["state"].values and answer_state not in states_guessed:
        cor_x = df_indexed.loc[answer_state, "x"]
        cor_y = df_indexed.loc[answer_state, "y"]
        writer.goto(cor_x, cor_y)
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))
        states_left -= 1
        states_guessed.append(answer_state)

turtle.TK.messagebox.showinfo(title="Congrats", message="You win!")
turtle.bye()