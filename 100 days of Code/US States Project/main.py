from turtle import Turtle, Screen
import pandas as pd

scr = Screen()
scr.screensize(200,200)
scr.title("US State")

image = "blank_states_img.gif"
scr.addshape(image)
tur = Turtle()
tur.shape(image) # used to add image on the screen

data = pd.read_csv("50_states.csv")

# def click_to_get_coord(x,y):
#     print(x, y)
#
# tur.onclick(click_to_get_coord) # use to get x and y coordinate

guessed_states= []
all_states = data.state.to_list()

while len(guessed_states) <= 50:
    answer_state = scr.textinput(title=f"{len(guessed_states)}/50 States Correctly", prompt="What's another State's name?").title()

    if answer_state == "Exit":
        break

    else:
        for i in data.state:
            if i in answer_state:
                guessed_states.append(i)
                tur = Turtle()
                tur.hideturtle()
                location = data[data.state == i]
                tur.penup()
                tur.speed("fastest")
                tur.goto(int(location.x), int(location.y))
                tur.write(i)

s = [state for state in all_states if state not in guessed_states]

states = pd.DataFrame(s)
states.to_csv("states_to_learn.csv")


scr.mainloop()