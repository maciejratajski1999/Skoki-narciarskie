from jumper import Jumper
from hill import Hill
import numpy as np
from matplotlib import pyplot as plt
from math import sin, cos

class SkiJumpAnimation:

    def __init__(self, hill):
        self.hill = hill
        self.delta_time = 1/1000
        self.time = np.arange(0,10,self.delta_time)
        self.hill_curve, self.hill_length = self.__draw_hill()
        plt.plot(self.hill_length, self.hill_curve)



    def __draw_hill(self):
        hill_length = np.arange(0, 1.5 * self.hill.length, 0.1)
        return [self.hill.curve(x) for x in hill_length], hill_length

    def __linear_model(self, v, mass, Cd, g, area=2):
        '''
        :param v: tuple (Vx(i), Vy(i))
        :param Cd: stała oporu powietrza
        :param mass: masa skoczka
        :param g: przyspieszenie ziemskie g
        :return : tuple (Vx(i+1),Vy(i+1))
        '''
        l = (v[0] ** 2 + v[1] ** 2) ** (1 / 2)
        Cd = Cd/mass
        area = self.__area(area,v)
        print(area)
        return -(Cd*1) * v[0]  * self.delta_time, (-(Cd*area) * v[1]  - g)  * self.delta_time

    def __square_model(self, v, mass, Cd, g, area):
        '''
        :param v: tuple (Vx(i), Vy(i))
        :param Cd: stała oporu powietrza
        :param mass: masa skoczka
        :param g: przyspieszenie ziemskie g
        :return : tuple (Vx(i+1),Vy(i+1))
        '''
        l = (v[0] ** 2 + v[1] ** 2) ** (1 / 2)
        Cd = Cd/mass
        return -(Cd*area[0]) * v[0]  * l* self.delta_time, (-(Cd*area[1]) * v[1] * l  - g)  * self.delta_time

    # def __area(self, area, v, l):
    #     return area * ((abs(v[1])) / l)


    def show(self, jumpers, cd, g, angle):
        color = 'b'
        for jumper in jumpers:
            Cd = cd
            VX, VY = [self.hill.velocity], [-0.05*self.hill.velocity]
            mass = jumper.mass
            area = jumper.area*sin(angle), jumper.area*cos(angle)

            for t in self.time[1:]:
                x, y = self.__square_model((VX[-1], VY[-1]), mass, Cd, g, area)
                # print(t)
                VX.append(VX[-1] + x)
                VY.append(VY[-1] + y)

            jumper.move(0, self.hill.height)
            X, Y = [jumper.position[0]], [jumper.position[1]]
            for i in range(1, len(self.time)):
                jumper.move(VX[i] * self.delta_time, VY[i] * self.delta_time)
                x, y = jumper.position[0], jumper.position[1]
                X.append(x)
                Y.append(y)
                if y <= self.hill.curve(x) or x > self.hill_length[-1]:
                    break
            plt.plot(X,Y)
        plt.show()
            # for i in range(0,len(X), 100):
            #     c = plt.Circle((X[i],Y[i]), 0.6, color=color)
            #     self.axs.add_artist(c)
            #     self.cnv.canvas.draw()
            #     plt.pause(self.delta_time*100)
            # color = 'r'





wisła = Hill(100,23)
okienko = SkiJumpAnimation(wisła)
okienko.show((Jumper(45),Jumper(55),Jumper(65)), cd=0.038, g=9.81, angle=0)


