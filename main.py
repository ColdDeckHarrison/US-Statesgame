import turtle
from turtle import Screen
import pandas


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
guessed_states = []
correct_guess = 0
while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{correct_guess}/50 Guess the State", prompt="What's another state?").title()
    if guess == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if guess in states:
        correct_guess += 1
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_state = data[data.state == guess]
        t.goto(int(data_state.x), int(data_state.y))
        t.pendown()
        t.write(guess)



