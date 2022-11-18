from turtle import Screen, Turtle
import time


class Snake:
    LIST_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.HEAD=self.segments[0]
        self.HEAD.color("red")
    def create_snake(self):
        for pos in self.LIST_COORDINATES:
            body_part = Turtle(shape="circle")
            body_part.color("white")
            body_part.penup()
            body_part.setpos(pos)
            self.segments.append(body_part)

    def extend_tail(self):
        new=self.segments[-1].pos()
        body_part = Turtle(shape="circle")
        body_part.color("white")
        body_part.penup()
        body_part.setpos(new)
        self.segments.append(body_part)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].setpos(x, y)
        self.segments[0].forward(20)

    # def teleport(self):



    def up(self):
        if self.segments[0].heading() != self.DOWN:
            self.segments[0].setheading(self.UP)

    def down(self):
        if self.segments[0].heading() != self.UP:
            self.segments[0].setheading(self.DOWN)

    def right(self):
        if self.segments[0].heading() != self.LEFT:
            self.segments[0].setheading(self.RIGHT)

    def left(self):
        if self.segments[0].heading() != self.RIGHT:
            self.segments[0].setheading(self.LEFT)

    def space(self):
        time.sleep(10)

    def play(self):
        self.screen.update()
        time.sleep(0.1)