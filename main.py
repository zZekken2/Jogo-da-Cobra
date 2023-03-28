import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

tr = turtle.Turtle()
tr.hideturtle()
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
'''screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)'''
screen.title("Python Game")
#screen.bgcolor("light blue") "white" ou "light blue"
screen.bgpic(r"grass-snake.png") #meter aqui caminho da imagem
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    food.flash()
    food.changestate()

#Detect collision from food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.new_tail()
        scoreboard.increase_score()

#If the tail and head collide
    for i in range(2, len(snake.segments)):
        if snake.head.distance(snake.segments[i].position()) < 20:
            game_is_on = False
            scoreboard.gameover()

#Wall collision
    if snake.head.xcor() > 940 or snake.head.xcor() < -940 or snake.head.ycor() > 530 or snake.head.ycor() < -530:
        game_is_on = False
        scoreboard.gameover()

screen.exitonclick()