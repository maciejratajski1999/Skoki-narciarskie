import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from jumper import Jumper
from hill import Hill
from math import sin, cos, atan

def jump(hill, jumper):

    v0 = hill.velocity
    v_angle = 0
    time = np.linspace(0,10, num=1000)
    delta_t = 10/1000


    def linear_model(v,t):
        cd = 1/jumper.mass
        return -cd*v[0], cd*v[1]-9.81

    def square_model(v,t):
        cd = 0.1 / jumper.mass
        l = (v[0]**2 + v[1]**2)**(1/2)
        return -cd*v[0]*l, cd*v[1]*l-9.81

    return odeint(square_model,[v0,0],time)

print(jump(Hill(100,23),Jumper(55)))

