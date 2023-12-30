import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bivariate_interpolation_complex(x, y, z, x_interp, y_interp):
    n = len(x)
    m = len(y)
    p = np.zeros_like(x_interp, dtype=complex)
    for k in range(n):
        for l in range(m):
            phi = np.ones_like(x_interp, dtype=complex)
            for i in range(n):
                if i != k:
                    phi *= (x_interp - x[i]) / (x[k] - x[i])
            for j in range(m):
                if j != l:
                    phi *= (y_interp - y[j]) / (y[l] - y[j])
            p += z[k, l] * phi
    return p

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 2, 3, 4])
z = np.exp(-x[:, np.newaxis] - 2j *(x[:, np.newaxis]+ y[np.newaxis, :])*y[np.newaxis, :])
x_interp = np.linspace(0, 4, 100)
y_interp = np.linspace(0, 4, 100)
x_interp, y_interp = np.meshgrid(x_interp, y_interp)
z_interp = bivariate_interpolation_complex(x, y, z, x_interp.ravel(), y_interp.ravel())
z_interp = z_interp.reshape(x_interp.shape)
print("Interpolated Values:")
for i in range(len(x_interp)):
    for j in range(len(y_interp)):
        print("x =", x_interp[i, j], "y =", y_interp[i, j], "z_interp =", z_interp[i, j])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_interp, y_interp, np.real(z_interp), cmap='viridis', linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Real(z)')
ax.set_title('Complex Function (Real Part)')

plt.show()
