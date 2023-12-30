import math
def fx(x:float)->float:
    res =(math.sqrt((math.pow(x,2))-1.0))/(pow(x,4))
    return res
def priamokutnyk(krok:float, a:float, b:float)->float:
    sum:float = 0.0
    n = int((b-a)/krok)
    x = a
    for i in range(n+1):
        sum+= fx(x)
        x+=krok
    return sum*krok
def trapetsiya(krok:float, a:float, b:float)->float:
    sum:float = 0.0
    x:float=1.0+krok
    for i in range(1,int((b-a)/krok),1):
        sum+= (fx(x)+fx(x+krok))*(krok/2)
        x+=krok
    return sum
def simpson3(a:float, b:float, q=100)->float:
    h = (b-a)/(2*q)
    sum:float = 0
    for i in range(0,2*q-1,2):
        if(i==0):
            sum+= fx(b)+4*fx(a+h*i)+fx(a+h*(i+1))
        else:
            sum+= fx(a+h*(i-1))+4*fx(a+h*i)+fx(a+h*(i+1))
    return sum*h/3
def fxx(x:float,y:float)->float:
    fx = 12*y*math.sin(2*x*y)
    return fx    
def cubic_simpson(x0:float, x1:float, y0:float, y1:float)->float:
    res = 0
    n = 2
    v_h = (x1 - x0)/4
    v_k = (y1 - y0)/4
    for i in range(n):
        for j in range(n):
            sigma0 = get_sigma0(x0 + i*2*v_h, y0 + j*2*v_k, v_h, v_k)
            sigma1 = get_sigma1(x0 + i*2*v_h, y0 + j*2*v_k, v_h, v_k)
            sigma2 = get_sigma2(x0 + i*2*v_h, y0 + j*2*v_k, v_h, v_k)
            res += sigma0 + 4 * sigma1 + 16 * sigma2
    res = res * v_h * v_k / 9
    return res
def get_sigma0(x0:float, y0:float, v_h:float, v_k:float)->float:
    return fxx(x0, y0) + fxx(x0 + 2*v_h, y0) + fxx(x0, y0 + 2*v_k) +fxx(x0 + 2*v_h, y0 + 2*v_k)
def get_sigma1(x0:float, y0:float, v_h:float, v_k:float)->float:
    return fxx(x0, y0+v_k) + fxx(x0 + 2*v_h, y0+v_k) + fxx(x0+v_h, y0) +fxx(x0+v_h, y0 + 2*v_k)
def get_sigma2(x0:float, y0:float, v_h:float, v_k:float)->float:
    return fxx(x0+v_h, y0+v_k)
#start
s1t:float = (math.sqrt(3.0))/8
toch1:float = (s1t/100)*2
s2t:float = -1.0
toch2:float = (s2t/100)*2
a:float = 1.0
b:float = 2.0
krok:float = 0.001
n:int = (b-a)/krok
a1:float = 2.0
a2:float = 3.0
krok1:float = 0.01
n1:int = (a2-a1)/krok1
b1:float = math.pi/4
b2:float = math.pi/2
krok2:float = 0.01
n2:int = (b2-b1)/krok2
i1 = priamokutnyk(krok,a,b)
print("Завдання 1:")
print()
print("Метод прямокутників:",i1)
print("Похибка: ",abs(i1-s1t))
print("2 відсотки: ",toch1)
i1 = trapetsiya(krok,a,b)
print("Метод трапецій:",i1)
print("Похибка: ",abs(i1-s1t))
print("2 відсотки: ",toch1)
i1 = simpson3(a,b)
print("Метод Симпсона:",i1)
print("Похибка: ",abs(i1-s1t))
print("2 відсотки: ",toch1)
print()
i1 = cubic_simpson(2.0, 3.0, (math.pi)/4, (math.pi)/2)
print("Завдання 2:")
print()
print("За кубаторною формулою Сімпсона: ", i1)
print("Похибка: ",abs(i1-s2t))
print("2 відсотки: ",abs(toch2))