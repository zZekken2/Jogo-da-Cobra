import turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) - 1]

    def create_snake(self):
        for position in STARTING_POS:
            python = turtle.Turtle()
            python.color("black")
            python.shape("square")
            python.pencolor("green")
            python.penup()
            python.speed(6)
            python.goto(position)

            self.segments.append(python)

    def new_tail(self):
        new_tail = turtle.Turtle()
        new_tail.speed(6)
        new_tail.shape("square")
        new_tail.color("black")
        new_tail.pencolor("green")
        new_tail.penup()

        x, y = self.tail.pos()

        if self.tail.heading()==UP:
            new_tail.goto(x, y-20)
        elif self.tail.heading()==RIGHT:
            new_tail.goto(x-20, y)
        elif self.tail.heading()==DOWN:
            new_tail.goto(x, y+20)
        elif self.tail.heading()==LEFT:
            new_tail.goto(x+20, y)

        self.segments.append(new_tail)
        self.tail=self.segments[len(self.segments) - 1]

    def move(self):
        for boxes in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[boxes - 1].xcor()
            new_y = self.segments[boxes - 1].ycor()
            self.segments[boxes].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)