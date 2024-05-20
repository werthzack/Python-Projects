import turtle
import random

class Road:
    def __init__(self):
        self.cars = []
        self.move_speed = 10
        self.prev_lane = 0

    def move_cars(self):
        for i in range(len(self.cars)):
            cur_car = self.cars[i]
            xcor = cur_car.xcor() - self.move_speed
            cur_car.goto(xcor, cur_car.ycor())
            if xcor > 300:
                cur_car.clear()
                self.cars.remove(cur_car)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        return color

    def select_lane(self):
        while True:
            sel_lane = random.randint(1, 10)
            if sel_lane != self.prev_lane:
                self.prev_lane = sel_lane
                return sel_lane

    def spawn_car(self):
        new_car = turtle.Turtle()
        new_car.penup()
        turtle.colormode(255)
        new_car.shape("square")
        new_car.color(self.random_color())
        new_car.shapesize(1, 2)
        lane = self.select_lane()
        ycor = -250 + (50 * lane)
        new_car.goto(300, ycor)
        self.cars.append(new_car)
