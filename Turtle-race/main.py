import turtle
import random

my_screen =turtle.Screen()
my_screen.setup(width=600,height=400)
user_choice= my_screen.textinput(title="Enter your bet",prompt="Which color of turtle will win?(red/blue/orange/yellow/green/purple)")
colors=[ "red", "orange", "yellow", "green","blue", "purple"]
ypos=[-100,-60,-20,20,60,100]
all_turtles=[]
speed=[]
for index in range(0,6):
    tup=turtle.Turtle() 
    tup.penup()
    tup.shape("turtle")
    tup.color(colors[index])
    tup.goto(x=-290,y=ypos[index])
    all_turtles.append(tup)
race_on=False
if user_choice:
    race_on=True

while race_on:
    for each_turtle in all_turtles:
        if each_turtle.xcor() > 270:
            race_on=False
            winner= each_turtle.pencolor()
            if winner==user_choice.lower():
                print(f"You have Won! {winner} turtle is the winner!")
            else:
                print(f"You have Lost! {winner} turtle is the winner!")

        each_turtle.forward(random.randint(0,10))



my_screen.exitonclick()