class Hill:

    def __init__(self, lenght, velocity):
        self.velocity = velocity
        self.length = lenght
        self.height = self.length*0.55
        self.modifier = -((1/(3*self.length))*(self.length**3) - (self.length**2))/(self.height +3)

    def curve(self, x):
        return ((1/(3*(self.length + 3)))*(x**3) - (x**2))/self.modifier + self.height - 3


