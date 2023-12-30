import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return 2.0
def q(x):
    return -1.5*x
def f(x):
    return(2/x)
a1,a2,A = 0,1,1
b1,b2,B = 1,2,1
def riznytsi(rozmah,h,func):
    xi = np.arange(rozmah[0],rozmah[1],h)
    size = len(xi)
    A_matrix = np.zeros((size, size))
    B_vector = np.zeros((size, 1))
    y1 = a2
    y0 = a1*h - a2
    yn_minus1 = - b2
    yn = b1 * h + b2
    A_matrix[0][0], A_matrix[0][1] = y0, y1
    A_matrix[-1][-2], A_matrix[-1][-1] = yn_minus1, yn
    B_vector[0] = A
    B_vector[-1] = B
    point = rozmah[0] + h
    for i in range(1, size-1):
        A_matrix[i][i] = func['yi'](point, h)
        A_matrix[i][i-1] = func['yi_minus1'](point, h)
        A_matrix[i][i+1] = func['yi_plus1'](point, h)
        B_vector[i] = func['fi'](point, h)
        point += h
    Y = np.linalg.solve(A_matrix, B_vector)
    return Y

def build_plot(X, Y):
    plt.plot(X, Y, 'y', label = 'solution')
    plt.plot(X, Y, 'm*', label = 'mesh nodes' )
    plt.title('Розв*язок крайової задачі')
    plt.legend()
    plt.show()

func = {'yi_plus1': lambda xi, h: 1 / h**2 + p(xi) / (2 * h),
'yi': lambda xi, h: -2 / h**2 + q(xi),
'yi_minus1': lambda xi, h: 1 / h ** 2 - p(xi) / (2 *h),
'fi': lambda xi, h: f(xi)}
h = 0.05
rozmah = (0.8, 1.1)
xi = np.arange(rozmah[0], rozmah[1], h)

y_solution = riznytsi(rozmah, h, func)
for i in range(7):
    print("y",i," = ",y_solution[i])
build_plot(xi, y_solution)