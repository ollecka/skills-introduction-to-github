#import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG game")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.paddle_up, "Up")
screen.onkeypress(paddle_r.paddle_down, "Down")
screen.onkeypress(paddle_l.paddle_up, "q")
screen.onkeypress(paddle_l.paddle_down, "a")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() < -380: # jeśli piłka w lewą ścianę
        ball.ball_init()
        score.r_point()
        score.update_scoreboard()
    elif ball.xcor() > 380: # jeśli w prawą
        ball.ball_init()
        score.l_point()
        score.update_scoreboard()
## ball.distance(paddle) mierzy odl do środka paddle
## szer. każdego to 20 pikseli

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        score.update_scoreboard()
screen.exitonclick()