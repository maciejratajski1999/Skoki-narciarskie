import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from jumper import Jumper
from hill import Hill

malysz = Jumper(100)
wisla = Hill(100, 25)



def move_jumper(jumper):
    for i in range(len(t)):
        x = Vx[i]*delta_t
        y = Vy[i]*delta_t
        jumper.move(x,y)
        X.append(jumper.position[0])
        Y.append(jumper.position[1])
        if jumper.position[1] <= 0:
            break

def simulate_jump(hill, *jumpers):

    hill_length = np.linspace(0, 2 * hill.length, 1000)
    hill_curve = [hill.curve(x) for x in hill_length]



    vy0 = 0
    vx0 = hill.velocity

    time = np.linspace(0,10, 10000)
    delta_time = 15/10000

    jumps = []

    for jumper in jumpers:
        def model_x(vx, t):
            m = jumper.mass
            drag_coefficient = 1 * 0.2 / m
            return -drag_coefficient * (vx ** 2)

        def model_y(vy, t):
            m = jumper.mass
            drag_coefficient = 1 * 0.2 / m
            g = 10
            return -g + drag_coefficient * (vy ** 2)
        VX = odeint(model_x, vx0, time)
        VY = odeint(model_y, vy0, time)
        jumper.move(0,hill.height)
        X,Y = [jumper.position[0]], [jumper.position[1]]

        for i in range(1, len(time)):
            jumper.move(VX[i]*delta_time, VY[i]*delta_time)
            X.append(jumper.position[0])
            Y.append(jumper.position[1])
            j = [x>=jumper.position[0] for x in hill_length].index(True)
            if Y[-1] <= hill_curve[j] or X[-1] > hill.length*2:
                break
        jumps.append([X,Y])
    return jumps, hill_length, hill_curve

jumps, hill_length, hill_curve = simulate_jump(wisla, malysz)

plt.plot(hill_length, hill_curve)

for jump in jumps:
    X,Y = jump[0], jump[1]
    plt.plot(X,Y)

plt.show()