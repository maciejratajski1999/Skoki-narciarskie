class Hill:

    def __init__(self, length, velocity):
        self.velocity = velocity
        self.length = length
        self.height = self.length*(0.6)
        self.draw_length = self.length*1.2
        self.modifier = -((1/(3*self.draw_length))*((self.draw_length)**3) - ((self.draw_length)**2))/self.height

    def curve(self, x):
        x= x + self.length*0.2
        return ((1/(3*(self.draw_length)))*(x**3) - (x**2))/self.modifier + self.height


