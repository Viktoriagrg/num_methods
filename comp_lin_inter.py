import numpy as np
import matplotlib.pyplot as plt

def linear_interp_complex(x, y, x_interp):
    interpolated = np.zeros_like(x_interp, dtype=complex)
    
    for i, xi in enumerate(x_interp):
        idx = np.searchsorted(x, xi)
        idx_left = idx - 1
        idx_right = idx
        x_left = x[idx_left]
        x_right = x[idx_right]
        y_left = y[idx_left]
        y_right = y[idx_right]
        weight = (xi - x_left) / (x_right - x_left)
        interpolated[i] = y_left + weight * (y_right - y_left)
    
    return interpolated

x = np.linspace(0, 1, 20)
z = x + 1j * 24 * x**2
x_interp = np.linspace(0, 1, 100)
z_linear = linear_interp_complex(x, z, x_interp)
print("Linear Interpolation:")
print(z_linear)
plt.plot(x, z.real, 'bo', label='Original (Real)')
plt.plot(x_interp, z_linear.real, label='Linear Interpolation (Real)')
plt.legend()
plt.xlabel('x')
plt.ylabel('z')
plt.title('Interpolation of Complex Function')
plt.show()
