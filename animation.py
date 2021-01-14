from jumper import Jumper
from hill import Hill
import numpy as np
from matplotlib import pyplot as plt

class SkiJumpAnimation:

    def __init__(self, hill):
        self.cnv, self.axs = plt.subplots()
        self.hill = hill
        self.delta_time = 1/1000
        self.time = np.arange(0,10,self.delta_time)
        self.hill_curve, self.hill_length = self.__draw_hill()
        plt.plot(self.hill_length, self.hill_curve)
        self.cnv.show()



    def __draw_hill(self):
        hill_length = np.arange(0, 1.5 * self.hill.length, 0.1)
        return [self.hill.curve(x) for x in hill_length], hill_length

    def __linear_model(self, v, mass, Cd, g):
        '''
        :param v: tuple (Vx(i), Vy(i))
        :param Cd: stała oporu powitrza
        :param mass: masa skoczka
        :param g: przyspieszenie ziemskie g
        :return : tuple (Vx(i+1),Vy(i+1))
        '''
        return -(Cd/mass) * v[0] * self.delta_time, (-(Cd/mass) * v[1] - g) * self.delta_time

    def show(self, jumpers, cd, g):
        color = 'b'
        for jumper in jumpers:
            Cd = cd / jumper.mass
            VX, VY = [self.hill.velocity], [0]
            mass = jumper.mass

            for t in self.time[1:]:
                x, y = self.__linear_model((VX[-1], VY[-1]), mass, Cd, g)
                VX.append(VX[-1] + x)
                VY.append(VY[-1] + y)

            jumper.move(0, self.hill.height)
            X, Y = [jumper.position[0]], [jumper.position[1]]
            for i in range(1, len(self.time)):
                jumper.move(VX[i] * self.delta_time, VY[i] * self.delta_time)
                x, y = jumper.position[0], jumper.position[1]
                X.append(x)
                Y.append(y)
                if y <= self.hill.curve(x) or x > self.hill.length * 2:
                    break

            for i in range(0,len(X), 100):
                c = plt.Circle((X[i],Y[i]), 0.6, color=color)
                self.axs.add_artist(c)
                self.cnv.canvas.draw()
                plt.pause(self.delta_time*100)
            color = 'r'


wisła = Hill(100,25)
okienko = SkiJumpAnimation(wisła)
okienko.show((Jumper(55),Jumper(100)), 0.2, 9.81)



