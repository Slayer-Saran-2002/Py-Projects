import time
from turtle import Screen
from snake import Snake
from food import Food
my_screen= Screen()
my_screen.setup(width=600,height=600)
my_screen.title("Python snake game")
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
foods=Food()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_on= True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    # Collision detector
    if snake.snake_head.distance(foods)<15:
        foods.refresh()




















my_screen.exitonclick()

