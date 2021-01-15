class Jumper:

    def __init__(self, mass):
        self.mass = mass
        self.area = 20
        self.position = 0,0

    def move(self, x, y):
        self.position = self.position[0] + x, self.position[1] + y
