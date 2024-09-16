import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US states Game")
image = "blank_states_img.gif"
screen.addshape(image) #This adds image shape to the screen
turtle.shape(image)

# def get_mouse_click_cor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()# This is alternative for screen.exitonclick() which works on clicks
#
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state name..", prompt="Enter the state name..").title()
    if answer_state == "Exit":
        for i in all_states:
            if i not in guessed_states:
                missing_states.append(i)
        break

    if answer_state in all_states:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        x_cor = int(state_data["x"].iloc[0])
        y_cor = int(state_data["y"].iloc[0])
        tim.goto(x_cor,y_cor)
        tim.write(answer_state)
        guessed_states.append(answer_state)
new_data = pd.DataFrame(missing_states)
new_data.to_csv("missing_states_data.csv")
screen.exitonclick()