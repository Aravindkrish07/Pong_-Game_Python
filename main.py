from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# set the initial screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

# movement of the ball just up and down
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)  # delay the movement of the ball, import time
    screen.update()  # to stop the motion of the animation, we need to setup tracer to 0 before hand
    ball.move()

    # detect the collision with the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # needs to bounce

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect collision right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect collision with left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
