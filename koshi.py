import math
import numpy as np
from matplotlib import pyplot as plt

def F(x, y):
    return 5.0+((2*x-5.0)/(x**2))*y
# Runge-Kut
def k0(x, y, h):
    return h*F(x, y)
def k1(x, y, h):
    return h*F(x + h/2., y + k0(x, y, h)/2.)
def k2(x, y, h):
    return h*F(x + h/2., y + k1(x, y, h)/2.)
def k3(x, y, h):
    return h*F(x + h, y + k2(x, y, h))
def Yrungekut(x, y, h):
    return y + 1./6*(k0(x, y, h) + 2*k1(x, y, h) + 2*k2(x, y, h) + k3(x, y, h))
def Yadams(x, y, h):
    return y[-2] + h*(9./24*F(x[-1], y[-1]) + 19./24*F(x[-2], y[-2]) - 5./24*F(x[1], y[1]) +1./24*F(x[0], y[0]))

h = 0.01
x = np.linspace(start = 2, stop = 3, num = int(1./h + 1), endpoint = True)
y = [(_**2) for _ in x ]
yRungeKut = [4]
for i in range(1, len(x)):
    yRungeKut += [ Yrungekut(x[i-1], yRungeKut[i-1], h) ]
yAdams = yRungeKut[:]
for i in range(3, len(x)):
    yAdams += [ Yadams(x[i-3:i+1], yAdams[i-3:i+1], h) ]
for i in range(len(x)):
    print('i={0}, x={1}, y={2}, yRungeKut={3}, yAdams={4}'.format(i, x[i], y[i], yRungeKut[i],yAdams[i]))
eRungeKut = [ abs(y[i] - yRungeKut[i]) for i in range(len(x)) ]
eAdams = [ abs(y[i] - yAdams[i]) for i in range(len(x)) ]

plt.plot(x, list(zip(y, yRungeKut, yAdams)))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['y', 'Runge-Kut', 'Adams'])
plt.show()

plt.plot(x, list(zip(eRungeKut, eAdams)))
plt.xlabel('x')
plt.ylabel('e')
plt.legend(['Runge-Kut', 'Adams'])
plt.show()
