from jumper import Jumper
from hill import Hill
import numpy as np
from matplotlib import pyplot as plt
from math import sin, cos, pi

class CompareJumpers:

    def __init__(self, hill):
        self.hill = hill
        self.delta_time = 1/1000
        self.time = np.arange(0,10,self.delta_time)
        self.hill_curve, self.hill_length = self.__draw_hill()
        plt.plot(self.hill_length, self.hill_curve)



    def __draw_hill(self):
        hill_length = np.arange(0, 1.5 * self.hill.length, 0.1)
        return [self.hill.curve(x) for x in hill_length], hill_length

    def __linear_model(self, v, Cd, g, area=2):
        '''
        :param v: tuple (Vx(i), Vy(i))
        :param Cd: stała oporu powietrza
        :param mass: masa skoczka
        :param g: przyspieszenie ziemskie g
        :return : tuple (Vx(i+1),Vy(i+1))
        '''
        # l = (v[0] ** 2 + v[1] ** 2) ** (1 / 2)
        return -(Cd*1) * v[0]  * self.delta_time, (-(Cd*area) * v[1]  - g)  * self.delta_time

    def __square_model(self, v, Cd, g, area):
        '''
        :param v: tuple (Vx(i), Vy(i))
        :param Cd: stała oporu powietrza
        :param mass: masa skoczka
        :param g: przyspieszenie ziemskie g
        :return : tuple (Vx(i+1),Vy(i+1))
        '''
        l = (v[0] ** 2 + v[1] ** 2) ** (1 / 2)
        return -(Cd*area[0]) * v[0]  * l* self.delta_time, (-(Cd*area[1]) * v[1] * l  - g)  * self.delta_time



    def show(self, jumpers, cd, g, angle):
        for jumper in jumpers:
            VX, VY = [self.hill.velocity*cos(-self.hill.angle)], [self.hill.velocity*sin(-self.hill.angle)]
            mass = jumper.mass
            Cd = cd / mass
            area = jumper.area*sin(angle), jumper.area*cos(angle)

            for t in self.time[1:]:
                x, y = self.__square_model((VX[-1], VY[-1]), Cd, g, area)
                VX.append(VX[-1] + x)
                VY.append(VY[-1] + y)

            jumper.move(0, self.hill.height+1)
            X, Y = [jumper.position[0]], [jumper.position[1]]
            for i in range(1, len(self.time)):
                jumper.move(VX[i] * self.delta_time, VY[i] * self.delta_time)
                x, y = jumper.position[0], jumper.position[1]
                X.append(x)
                Y.append(y)
                if y <= self.hill.curve(x) or x > self.hill_length[-1]:
                    break
            plt.plot(X,Y)
            x, y = X[-1], Y[-1]
            plt.annotate(str(int(x * 2) / 2) + "m", (x, y))
        masses = [None]+[str(jumper.mass) + "kg" for jumper in jumpers]
        plt.legend(masses)
        plt.show()

# wisła = Hill(100,23, 0.1)
# okienko = CompareJumpers(wisła)
# okienko.show((Jumper(45),Jumper(55),Jumper(65)), cd=0.042, g=9.81, angle=pi/64)






