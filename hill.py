class Hill:

    def __init__(self, length, velocity):
        '''
        :param length: horyzontalny dystans od progu do punktu K
        :param velocity: prędkość wyjścia z progu
        '''
        self.velocity = velocity
        self.length = length
        self.height = self.length*(0.6)
        self.draw_length = self.length*1.25
        self.modifier = -(-(2/3)*((self.draw_length)**2))/self.height

    def curve(self, x):
        '''
        :return: wielomian trzeciego stopnia od x
        '''
        # nie chcem zaczynać z x=0, ponieważ oczekujemy że stok pod progiem od razu będzie nachylony
        x= x + self.length*0.2
        return ((1/(3*(self.draw_length)))*(x**3) - (x**2))/self.modifier + self.height
