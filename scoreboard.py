from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

score = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    def add(self):
        self.score+=1
        self.clear()
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)