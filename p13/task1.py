class Ball:
    color: tuple = (0, 0, 0)
    radius: int = 0
    weight: float = 0
    x: int = 0
    y: int = 0
    speed_x: int = 0
    speed_y: int = 0

    def __init__(self, radius: int, weight: float):
        if radius > 0:
            self.radius = radius
        else:
            print('Error! radius cannot less zero')

        if weight > 0:
            self.weight = weight

    def move_x(self):
        self.x += self.speed_x

    def move_y(self):
        self.y += self.speed_y


ball_1 = Ball(5, 20)
ball_1.radius = 40
print(ball_1.radius)
