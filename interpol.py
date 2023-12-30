import math
import numpy as np

def function(x: float):
    func = (math.log1p(x))/(x**3)
    return func

def Lagrange(x, r, n):
    result = 0.0
    for i in range(n):
        q = 1.0
        for j in range(n):
            if(i!=j):
               q *=((x-r[j])/(r[i]-r[j]))
        result+=q*function(r[i])
    return result

def Newton_F(x, r, n):
    result = function(r[0])
    A: float 
    w: float
    for i in range(n):
        A=0.0
        for j in range(i):
            w=1.0
            for k in range(i):
                if(k!=j):
                    w*=(r[j]-r[k])
            A+=function(r[j])/w
        for k in range(i):
            A*=(x-r[k])
        result += A
    return result

def Newton_B(x, r, n):
    result = function(r[n-1])
    A: float 
    w: float
    for i in range(n-2,-1,-1):
        A=0.0
        for j in range(n-1,i-1,-1):
            w=1.0
            for k in range(n-1, i-1,-1):
                if(k!=j):
                    w*=(r[j]-r[k])
            A+=function(r[j])/w
        for k in range(n-1,i,-1):
            A*=(x-r[k])
        result += A
    return result

def splain3(x, r, n):
    class spline_coef:
        a: float
        b: float
        c: float
        d: float
    spline = [spline_coef() for _ in range(n)]
    for i in range(n):
        spline[i].a = function(r[i])
    spline[0].c = 0.0
    alfa = [0.0 for _ in range(n)]
    beta = [0.0 for _ in range(n)]
    a_up, b_up, c_up, d_up, f_up, h_i, h_ii, z = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for i in range(1,n-1,1):
        h_i = r[i]-r[i-1]
        h_ii = r[i + 1] - r[i];
        a_up = h_i;
        c_up = 2 * (h_i + h_ii);
        b_up = h_ii;
        f_up = 6 * ((function(r[i + 1]) - function(r[i])) / h_ii - (function(r[i]) - function(r[i - 1])) / h_i);
        z = (a_up * alfa[i - 1] + c_up);
        alfa[i] = -b_up / z;
        beta[i] = (f_up - a_up * beta[i - 1]) / z;
    spline[n-1].c = (f_up - a_up *beta[n-2])/(c_up+a_up*alfa[n-2])
    for i in range(n-2,0,-1):
        spline[i].c = alfa[i]*spline[i+1].c + beta[i]
    for i in range(n-1,0,-1):
        h_i = r[i]-r[i-1]
        spline[i].d = (spline[i].c - spline[i-1].c) / h_i
        spline[i].b = h_i * (2 * spline[i].c + spline[i - 1].c) / 6 +(function(r[i]) - function(r[i - 1])) / h_i
    if x <= r[0]:
        s = spline[1]
        p = r[1]
    elif x >= r[n-1]:
        s = spline[n - 1]
        p = r[n-1]
    else:
        i = 0
        j = n-1
        while i+1<j:
            k = i+(j-i)//2
            if x<r[k]:
                j=k
            else:
                i=k
        s = spline[j]
        p = r[j]
    dx = x-p
    return s.a + s.b * dx + s.c * dx*dx/2 + s.d * dx*dx*dx/6

def f_4(x):
    return 126*(x**(-8))*(-x-6*x*math.log1p(x))-6*(x**(-7))-18*(x**(-7))*(-6*math.log1p(x)-7)-336*(x**(-9))*((x**2)-3*math.log1p(x)*(x**2))

def major(x, r, n):
    w =1.0
    for i in range(n):
        w*=x-r[i]
    return math.fabs(w)*math.fabs(f_4(r[0]))/720
#start
a = 1/4
b = 3.0
h = 1
n = 5
r = [0.0 for _ in range(n)]
k=0.0
for i in range(n):
   k+=h
   r[i]=k
x = r[0]
for i in range(22):#step 1/8
    print("------------------------------")
    print(f"x = {x}")
    print(f"Значення функції: {function(x)}")
    print(f"Значення інтерполяційного поліному Лагранжа: {Lagrange(x,r,n)}")
    print(f"Різниця: {math.fabs(function(x) - Lagrange(x, r, n))}")
    print(f"Значення інтерполяційного поліному Ньютона вперед:{Newton_F(x, r, n)}")
    print(f"Різниця: {math.fabs(function(x) - Newton_F(x, r, n))}")
    print(f"Значення інтерполяційного поліному Ньютона назад:{Newton_B(x, r, n)}")
    print(f"Різниця: {math.fabs(function(x) - Newton_B(x, r, n))}")
    print(f"Значення інтерполяційного сплайну: {splain3(x, r, n)}")
    print(f"Різниця: {math.fabs(function(x) - splain3(x, r, n))}")
    print(f"Мажоранта: {major(x, r, n)}")
    x = x + 1/8