from turtle import Screen, Turtle
import time
import snake, food , scoreboard

screen = Screen()
heading = Turtle()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("SnakeSss")
screen.tracer(0)


s = snake.Snake()
f = food.Food()
scr=scoreboard.Scoreboard()
screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")
screen.onkey(s.space, "space")
screen.onkey(s.play, "X")

game_is_on = True
scr.score()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.HEAD.distance(f) <= 15:
        f.refresh()
        scr.scoreupdate()
        s.extend_tail()

    if  s.HEAD.xcor() > 290 or s.HEAD.xcor() < -290 or s.HEAD.ycor() < -290 or s.HEAD.ycor() > 290:
        game_is_on=False
        scr.game_over()
    for segment in s.segments[1:]:
        if s.HEAD.distance(segment) <5:
            game_is_on = False
            scr.game_over()

    # if s.HEAD.xcor() > 290 or s.HEAD.ycor() == 0:

screen.exitonclick()
