import math
import numpy as np
import matplotlib.pyplot as plt
a = 0.7
q = 0.8
L = 0.8
T = 6

def u_0(x):
    return 0.4*math.sin(math.pi*x/L)

def u(x, t):
    return 0.4*math.exp(-t*11.5839375)*math.sin(math.pi*x/L)
def CrankNicolson(I, f, nt, nx):
    t = np.linspace(0, T, nt+1)
    x = np.linspace(0, L, nx+1)
    dx = x[1] - x[0]
    dt = t[1] - t[0]
    u = np.zeros(nx+1)
    u_n = np.zeros(nx+1)
    for i in range(0, nx+1):
        u_n[i] = I(x[i])
    for n in range(0, nt+1):
        for i in range(1, nx):
            u[i] = u_n[i] + a*(u_n[i-1] - 2*u_n[i] + u_n[i+1])*dt/dx**1 -   q*f(x[i], t[n])*dt
        u[0] = 0
        u[nx] = 0
        print(f"t={t[n]}:\nu={u}")
        u_n, u = u, u_n
    return u_n, x, t
u_n, x, t = CrankNicolson(u_0, u, 100, 10)
def err(u_n, x, t, f):
    res = []
    for i in range(len(u_n)):
        res.append(abs(u_n[i] - f(x[i], t[-1])))
    return res

u_err = err(u_n, x, t, u)
fig, ax = plt.subplots()
ax.plot(x, u_n)
ax.set(xlabel='x', ylabel='e')
ax.grid()
plt.show()
