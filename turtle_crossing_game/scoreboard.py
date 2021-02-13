from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align = "left", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align = "center", font = FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
