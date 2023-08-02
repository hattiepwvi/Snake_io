from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.high_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def high_scoreboard(self):
        with open("high_score.txt", "rb") as f:
            data = f.read()
            high_score_str = data.decode()
            self.high_score = int(high_score_str)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        with open("high_score.txt", "wb") as f:
            if self.high_score < self.score:
                high_score = str(self.score)
            else:
                high_score = str(self.high_score)
            f.write(high_score.encode())

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
