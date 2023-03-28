from turtle import Turtle
import random
import time

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.state="ON"
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
        self.last_state_change = time.time()

    def flash(self):
        if self.state=="ON":
            self.color("dark green")
        else:
            self.color("dark red")

    def refresh(self):
        random_x = random.randint(-600, 600)
        random_y = random.randint(-355, 355)
        self.goto(random_x, random_y)

    def changestate(self):
        elapsed_time = time.time() - self.last_state_change
        if elapsed_time >= 0.25:
            self.last_state_change = time.time()
            if self.state == "ON":
                self.state = "OFF"
            else:
                self.state = "ON"