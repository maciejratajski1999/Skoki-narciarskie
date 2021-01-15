import numpy


class Hill:

    def __init__(self, length, velocity, angle=0):
        '''
        :param length: horyzontalny dystans od progu do punktu K
        :param velocity: prędkość wyjścia z progu
        :param angle: kąt wyjścia z progu w radianach
        '''
        self.velocity = velocity
        self.length = length
        self.draw_length = self.length * 1.25
        self.difference = self.draw_length - self.length
        self.height = self.length * (self.length / 180)
        self.modifier = ((2 / 3) * ((self.draw_length) ** 2)) / (self.height)
        self.angle = angle

    def curve(self, x):
        '''
        :return: wielomian trzeciego stopnia od x
        '''
        # nie chcemy zaczynać z x=0, ponieważ oczekujemy że stok pod progiem od razu będzie nachylony
        x = x + self.difference
        return ((1 / (3 * (self.draw_length))) * (x ** 3) - (x ** 2)) / self.modifier + self.height

    def distance(self, a):
        # przybliża odległość skoku, dla punktu lądowania o x-owej współrzędnej a
        delta_x = 1
        xs = numpy.arange(0, a, delta_x)
        ys = [self.curve(x) * delta_x for x in xs]
        surface = [((ys[i] - ys[i - 1]) ** 2 + delta_x ** 2) ** (1 / 2) for i in range(1, len(ys))]
        return sum(surface)