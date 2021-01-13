import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from jumper import Jumper
from hill import Hill

malysz = Jumper(55)
wisla = Hill(100, 25)

def simulate_jump(hill, *jumpers):

    hill_length = np.linspace(0, 1.5 * hill.length, 1000)
    hill_curve = [hill.curve(x) for x in hill_length]

    vy0 = -0.5
    vx0 = hill.velocity
    delta_time = 1 / 1000
    time = np.arange(0,10, delta_time)

    jumps = []

    for jumper in jumpers:
        def linear_model(v):
            cd = 0.1 / jumper.mass
            return -cd*v[0]*delta_time, (-cd * v[1] - 9.81)*delta_time
        def square_model(v):
            cd = 0.02 / jumper.mass
            l = (v[0] ** 2 + v[1] ** 2) ** (1 / 2)
            return -cd * v[0] * l*delta_time, (-cd * v[1] * l - 9.81)*delta_time

        VX, VY = [vx0], [vy0]
        for t in time:
            x, y = square_model([VX[-1], VY[-1]])
            print(x,y)
            VX.append(VX[-1] + x)
            VY.append(VY[-1] + y)
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
plt.title("Gx : Gy = 1:1")
plt.show()