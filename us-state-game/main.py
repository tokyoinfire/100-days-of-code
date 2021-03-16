import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "USA.gif"
screen.addshape(image)

turtle.shape(image)

states_info = pandas.read_csv("50_states.csv")
us_states = states_info["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",
                                    prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in us_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in us_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = states_info[states_info.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
