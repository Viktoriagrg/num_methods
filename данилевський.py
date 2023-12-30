eps = 0.00001
class Polynom:
    def __init__(self, coeff, eps):
        coeff.reverse()
        self.coeff = coeff
        self.count = len(coeff)
        self.eps = eps
    def value(self, x):
        value = 0
        for i in range(self.count):
            value += self.coeff[i] * x**i
        return value
    def Bisection(self, a, b):
        iter = 1
        c = (a + b) / 2
        while not (abs(b - a) < self.eps and abs(self.value(c)) < self.eps):
            c = (a + b) / 2
            if self.value(a) * self.value(c) < 0:
                b = c
            else:
                a = c
            iter += 1
        return c, iter
def det3(matr):
        products = [matr[0][0] * matr[1][1] * matr[2][2],matr[2][0] * matr[0][1] * matr[1][2],matr[0][2] * matr[1][0] *matr[2][1],- matr[2][0]* matr[1][1] * matr[0][2],- matr[2][2] * matr[1][0] * matr[0][1],- matr[0][0]* matr[1][2] * matr[2][1]]
        sum = 0
        for p in products:
            sum += p
        return sum
def inverse4(matr):
        det = 1
        inv_matr = [[None for _ in range(4)] for _ in range(4)]
        for i in range(4):
            m = matr[0:i] + matr[i+1:4]
            m = [row[1:4] for row in m]
            det += (-1) ** i * matr[i][0] * det3(m)
        for i in range(4):
            for j in range(4):
                m = matr[0:j] + matr[j+1:4]
                m = [row[0:i] + row[i+1:4] for row in m]
                inv_matr[i][j] = (-1) ** (i + j) * det3(m) / abs(det)
        return inv_matr
def multiply(matr1, matr2):
        res_matr = [[0 for _ in range(len(matr2[0]))] for _ in range(len(matr1))]
        for i in range(len(res_matr)):
            for j in range(len(res_matr[0])):
                for k in range(len(matr1[0])):
                    res_matr[i][j] += matr1[i][k] * matr2[k][j]
        return res_matr
def lambda_(matr, eps):
        l = 1
        y = [[1], [1], [1], [1]]
        yk = multiply(matr, y)
        lk = yk[0][0] / y[0][0]
        k = 1
        while abs(lk - l) >= eps:
            y = yk
            yk = multiply(matr, y)
            l = lk
            lk = yk[0][0] / y[0][0]
            k += 1
        x = matrByScalar(1 / (lk ** k), yk)
        return lk, x
def matrByScalar(scalar, matr):
        for i in range(len(matr)):
            for j in range(len(matr[0])):
                matr[i][j] *= scalar
        return matr
def difference(a, b):
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] -= b[i][j]
        return a
def Danilevski(matr, l_array):
        matr_copy = [matr[i][:] for i in range(4)]
        E = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        B1 = [E[i][:] for i in range(4)]
        B2 = [E[i][:] for i in range(4)]
        B3 = [E[i][:] for i in range(4)]
        B1_inv = [E[i][:]for i in range(4)]
        B2_inv = [E[i][:]for i in range(4)] 
        B3_inv = [E[i][:]for i in range(4)]
        for i in range(4):
            B1[2][i] = - matr[3][i] / matr[3][2]
            print("matrix B1")
            printm(B1)
        B1[2][2] = 1 / matr[3][2]
        B1_inv[2] = matr[3][:]
        matr = multiply(multiply(B1_inv, matr), B1)
        for i in range(4):
            B2[1][i] = - matr[2][i] / matr[2][1]
            print("matrix B2")
            printm(B2)
        B2[1][1] = 1 / matr[2][1]
        B2_inv[1] = matr[2][:]
        matr = multiply(multiply(B2_inv, matr), B2)
        for i in range(4):
            B3[0][i] = - matr[1][i] / matr[1][0]
            print("matrix B3")
            printm(B3)
        B3[0][0] = 1 / matr[1][0]
        B3_inv[0] = matr[1][:]
        matr = multiply(multiply(B3_inv, matr), B3)
        print("matrix A")
        printm(matr)
        coeff = [1] + [-i for i in matr[0]]
        print("coef",coeff)
        coeff1 = [1, 0, 0, 0]
        for i in range(1, 4):
            coeff1[i] = l_array[0] * coeff1[i - 1] + coeff[i]
            print("coef1",coeff1)
        coeff2 = [1, 0, 0]
        for i in range(1, 3):
            coeff2[i] = l_array[3] * coeff2[i - 1] + coeff1[i]
            print("coef2",coeff2)
        D = coeff2[1] ** 2 - 4 * coeff2[0] * coeff2[2]
        l_array[1] = (- coeff2[1] + D ** 0.5) / (2 * coeff2[0])
        l_array[2] = (- coeff2[1] - D ** 0.5) / (2 * coeff2[0])
        polynom = Polynom(coeff, eps)
        l_array = [polynom.Bisection(l_array[i] - 0.1, l_array[i] + 0.1)[0] for i in range(4)]
        B = multiply(multiply(B1, B2), B3)
        y = [None for _ in range(4)]
        for i in range(4):
            y0 = [[l_array[i] ** (3 - j)] for j in range(4)]
            y[i] = multiply(B, y0)
        print("y")
        print(y[0])
        print(y[1])
        print(y[2])
        print(y[3])
        return l_array, y
def norm(matr):
        sum = 0
        for row in matr:
            for el in row:
                sum += el ** 2
        return sum ** 0.5
def printm(matr):
    print("\n")
    for i in range(len(matr)):
        for j in range(len(matr)):
            print("%.6f"%matr[i][j],end="  ")
        print("\n")

matr = [[6.48,1.2,0.87,1.21],
             [1.2,3.94,1.3,0.16],
             [0.87,1.3,5.66,2.1],
             [1.21,0.16,2.1,5.88]]
l1 = lambda_(matr, eps)
x1_error = difference(multiply(matr, l1[1]), matrByScalar(l1[0], l1[1]))
l4 = lambda_(inverse4(matr), eps)
x4_error = difference(multiply(matr, l4[1]), matrByScalar(1 / l4[0], l4[1]))
l_array = [l1[0], 0, 0, 1 / l4[0]]
print("Розв'язок часткової проблеми власних значень, використовуючи степеневий метод:")
print("λ(max) = %.6f\tv1 = (%.6f, %.6f, %.6f, %.6f)T" % (l_array[0], l1[1][0][0],
l1[1][1][0], l1[1][2][0], l1[1][3][0]))
print("x = Av1 – λv1 = (%.2e, %.2e, %.2e, %.2e)T\t║x║ = %.2e\n" % (x1_error[0][0],
x1_error[1][0], x1_error[2][0], x1_error[3][0], norm(x1_error)))
print("λ(min) = %.6f\tv4 = (%.6f, %.6f, %.6f, %.6f)T" % (l_array[3], l4[1][0][0],
l4[1][1][0], l4[1][2][0], l4[1][3][0]))
print("x = Av4 – λv4 = (%.2e, %.2e, %.2e, %.2e)T\t║x║ = %.2e\n" % (x4_error[0][0],
x4_error[1][0], x4_error[2][0], x4_error[3][0], norm(x4_error)))
print("\nРозв'язок повної проблеми, використовуючи метод Данилевського):")
[l_array, y] = Danilevski(matr, l_array)
subscript = ["1", "2", "3", "4"]
print("\nРезультат розв'язку повної проблеми, використовуючи метод Данилевського):")
for i in range(4):
    print("λ%s = %.6f\tx%s = (%.6f, %.6f, %.6f, %.6f)T" % (subscript[i], l_array[i], subscript[i], y[i][0][0], y[i][1][0], y[i][2][0], y[i][3][0]))
    x_error = difference(multiply(matr, y[i]), matrByScalar(l_array[i], y[i]))
    print("x = Ax%s – λx%s = (%.2e, %.2e, %.2e, %.2e)T\t║x║ = %.2e\n" % (subscript[i], subscript[i], x_error[0][0], x_error[1][0], x_error[2][0], x_error[3][0], norm(x_error)))
