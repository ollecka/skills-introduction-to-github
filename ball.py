from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        # self.setpos(0,0)
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        # self.speed(1)
        print(self.pos())
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        ## za każdym razem jest zmiana znaku parametru Y
        self.y_move *= -1
        # new_x = self.xcor() + self.x_move
        # new_y = self.ycor() - self.y_move
        # self.goto(new_x, new_y)

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_init(self):
        # self.setpos(0,0) # to moje, dlaczego ona uzywa goto??
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.1

## do testów:
# from turtle import Screen
# s = Screen()
# s.bgcolor("black")
# ball = Ball()
# ball.ball_move()
#
# s.exitonclick()