import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from jumper import Jumper
from hill import Hill

malysz = Jumper(55)
wisla = Hill(100, 23)

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
            drag_coefficient = 0.03 / m
            return -drag_coefficient * (vx ** 2)

        def model_y(vy, t):
            m = jumper.mass
            drag_coefficient = 0.6 / m
            g = 9.81
            return -g + drag_coefficient * (vy ** 2)
        VX = odeint(model_x, vx0, time)
        VY = odeint(model_y, vy0, time)
        jumper.move(0,hill.height + 3)
        X,Y = [jumper.position[0]], [jumper.position[1]]

        for i in range(1, len(time)):
            jumper.move(VX[i]*delta_time, VY[i]*delta_time)
            x,y = jumper.position[0],jumper.position[1]
            X.append(x)
            Y.append(y)

            if y <= hill.curve(x) or x > hill.length*2:
                break
        jumps.append([X,Y])
    return jumps, hill_length, hill_curve

jumps, hill_length, hill_curve = simulate_jump(wisla, Jumper(40), malysz, Jumper(70))


fig,ax = plt.subplots()
plt.plot(hill_length, hill_curve)

for jump in jumps:
    X,Y = jump[0], jump[1]
    plt.plot(X,Y)
    x,y = X[-1],Y[-1]
    ax.annotate(str(int(x*2)/2), (x,y))

plt.legend(["ląd","40kg","55kg","70kg"])
plt.axis('equal')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()