# import colorgram

# rgb_colors = []
# colors = colorgram.extract('F:\Python\~Projects\Hirst_painting\dot-img.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

# print(rgb_colors)
import turtle
import random

mycolor = [(188, 19, 46), (243, 232, 66), (251, 230, 236), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (148, 209, 220), (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187)]

tut = turtle.Turtle()
tut.shape("classic")
tut.color("black")
tut.speed("fastest")
turtle.colormode(255)
my_screen =turtle.Screen()
tut.penup()
tut.setheading(225)
tut.forward(350)
tut.setheading(0)
for i in range(1,101):
    tut.dot(20,random.choice(mycolor))
    tut.forward(50)
    if i%10==0:
        tut.setheading(90)
        tut.forward(50)
        tut.setheading(180)
        tut.forward(500)
        tut.setheading(0)


my_screen.exitonclick()