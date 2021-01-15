class Jumper:

    def __init__(self, mass):
        self.mass = mass # kg
        # ponieważ przyspieszenie działające na skoczka jest odwrotne proporcjonalnie do jego masy,
        # możemy nadmiar masy zrekompensować zwiększając jego powierzchnię
        # niech powierzchnia wynosi 2m^2 dla skoczka ważącego 55kg
        self.area = 2*(self.mass/55)    # m^2
        self.position = 0,0

    def move(self, x, y):
        self.position = self.position[0] + x, self.position[1] + y
