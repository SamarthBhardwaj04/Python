from turtle import Turtle
alignment='center'
font="Courier"
class Scoreboard(Turtle):
    # sb=Turtle()
    # sb.
    # sb.hideturtle()

    def score(self):
        super().__init__()
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 280)
        self.write(f"score: {self.score}", move=False, align=alignment, font=(font,12, "normal"))

    def scoreupdate(self):

        self.clear()
        self.score += 1
        self.write(f"score: {self.score}", move=False, align=alignment, font=(font,12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=alignment, font=(font, 25, "normal"))