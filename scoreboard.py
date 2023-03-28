from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.write(f"Score: {self.score}", True, align="center", font=("Karmatic Arcade", 24, "italic", "bold"))

    def gameover(self):
        self.goto(0,30)
        self.clear()
        self.color("black")
        self.write("Game Over", align="center", font=("Karmatic Arcade", 30, "bold"))
        self.goto(0,-60)
        self.write(f"Score: {self.score}", True, align="center", font=("Karmatic Arcade", 24, "bold"))

    def increase_score(self):
        self.goto(0,400)
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", True, align="center", font=("Karmatic Arcade", 24, "italic", "bold"))
