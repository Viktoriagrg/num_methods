import math
import copy

class Polinom:
    def __init__(self, koef, poh_koef):
        self.koef = koef
        self.poh_koef = poh_koef

    def fx(self, x):
        res = 0
        for i in reversed(range(len(self.koef))):
            res+=self.koef[i]*pow(x, len(self.koef)-i-1)
        return res

    def fshx(self,x):
        res = 0
        for i in reversed(range(len(self.poh_koef))):
            res+=self.poh_koef[i]*pow(x, len(self.poh_koef)-i-1)
        return res

    def Bissection(self, eps, promizhok):
        print("Bissection method")
        a = 0 # counter
        prom = copy.copy(promizhok)
        while True:
            a+=1
            sered_prom = (prom[0]+prom[1])/2
            print('%.2d' % a, "iteration. Left limit of interval = ", '%.15f.' % prom[0], "\nRight limit of interval = ", '%.15f.' % prom[1], "\nA value of function on the middle of interval is ", '%.5E'% self.fx(sered_prom))
            if math.fabs(self.fx(sered_prom))<=eps:
                break
            if self.fx(prom[0])*self.fx(sered_prom)<0:
                prom[1]=sered_prom
            else:
                prom[0]=sered_prom
        print("Result of Bissection method: x = " '%.15f,'%sered_prom, "f(x) = "'%5E'%self.fx(sered_prom), "\n\n\n\n\n\n")
        return

    def Chord_method(self, eps, promizhok):
        print("Chord_method")
        a = 0 # counter
        prom = copy.copy(promizhok)
        while True:
            c = (prom[0]*self.fx(prom[1]) - prom[1]*self.fx(prom[0]))/(self.fx(prom[1]) - self.fx(prom[0]))
            a+=1
            print('%.2d' % a, "iteration. Left limit of interval = ", '%.15f.' % prom[0], "\nRight limit of interval = ", '%.15f.' % prom[1], "\nA value of function from the intersection of chord with abscise axis is ", '%.5E'% self.fx(c))
            if math.fabs(self.fx(c))<=eps:
                break
            if self.fx(prom[0])*self.fx(c)<0:
                prom[0] = c
            else:
                prom[1] = c
        print("Result of Chord method: x = " '%.15f,'%c, "f(x) = "'%5E'%self.fx(c), "\n\n\n\n\n\n")
        return 

    def Newton_method(self, eps, promizhok):
        print("Newton_method")
        a = 0 # counter
        while True:
            if self.fshx(promizhok[1])==0:
                print("a derivative equals a zero")
                return
            a+=1
            xn = promizhok[1]-self.fx(promizhok[1])/self.fshx(promizhok[1])
            print('%.2d' % a, "iteration. Left limit of interval = ", '%.15f.' % promizhok[0], "\nRight limit of interval = ", '%.15f.' % promizhok[1], "\nA value of function from the intersection of tangent with abscise axis is ", '%.5E'% self.fx(xn))
            if math.fabs(self.fx(xn)) <= eps:
                break
            promizhok[1] = xn
        print("Result of Newton method: x = " '%.15f,'%xn, "f(x) = "'%5E'%self.fx(xn), "\n\n")  
        return 

# prog
Polinom = Polinom([27.5625,1323,19428.0625,85165.5,114244],[110.25,3969,38856.125,85165.5])
eps = 0.001
interval = [-40,-30]
#Polinom.Bissection(eps,interval)
#Polinom.Chord_method(eps,interval)
Polinom.Newton_method(eps,interval)
