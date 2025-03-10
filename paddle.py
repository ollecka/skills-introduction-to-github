from turtle import Turtle
UP = 90
DOWN = 270
MOVE_DIST = 20

class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.setpos(coordinates)
        self.turtlesize(stretch_len=1, stretch_wid=5)
        """ turtle ma wymiary 20 na 20; żeby paddle miało 100 na 20 to mnożymy przez 1 i 5"""
        self.speed("normal")

    def paddle_up(self):
        # self.setheading(UP) # to mi przekręca paddle o 90 st
        # self.forward(MOVE_DIST)
        new_y = self.ycor() +  MOVE_DIST
        self.goto(self.xcor(), y=new_y)


    def paddle_down(self):
        # self.setheading(DOWN) # to mi przekręca paddle o 90 st
        # self.forward(MOVE_DIST)
        new_y = self.ycor() - MOVE_DIST
        self.goto(self.xcor(), y=new_y)
