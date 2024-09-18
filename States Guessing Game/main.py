import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game")

img = "blank_states_img.gif"
turtle.addshape(img)
turtle.shape(img)



data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states  = []

print(states)


while len(guessed_states) <50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()


    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)






