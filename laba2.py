import math
import copy
class Matrix:
    def __init__(self, mat1, ends):
        self.mat1 = mat1
        self.ends = ends
    def max1(self):
        q = self.mat1[0][0]
        m = 0
        n = 0
        for i in range(len(self.mat1)):
            for j in range (len(self.mat1[i])):
                if q<self.mat1[i][j]:
                    q = self.mat1[i][j]
                    m=i
                    n=j
        if q == 0:
            q=-100
            for i in range(len(self.mat1)):
                for j in range (len(self.mat1[i])):
                    if (q<self.mat1[i][j] and self.mat1[i][j]!=0):
                        q = self.mat1[i][j]
                        m=i
                        n=j
        if q==-100:
            q=0
        return q,m,n
    def sum(self):
        s0,s1,s2,s3,s4=0,0,0,0,0
        s0 = self.mat1[0][0]+self.mat1[0][1]+self.mat1[0][2]+self.mat1[0][3]+self.mat1[0][4]+self.ends[0]
        s1 = self.mat1[1][0]+self.mat1[1][1]+self.mat1[1][2]+self.mat1[1][3]+self.mat1[1][4]+self.ends[1]
        s2 = self.mat1[2][0]+self.mat1[2][1]+self.mat1[2][2]+self.mat1[2][3]+self.mat1[2][4]+self.ends[2]
        s3 = self.mat1[3][0]+self.mat1[3][1]+self.mat1[3][2]+self.mat1[3][3]+self.mat1[3][4]+self.ends[3]
        s4 = self.mat1[4][0]+self.mat1[4][1]+self.mat1[4][2]+self.mat1[4][3]+self.mat1[4][4]+self.ends[4]
        return s0,s1,s2,s3,s4
    def printedmat(self,ma):
        for i in range(len(ma)):
            for j in range(len(ma[i])):
                print(ma[i][j],end=' ')
            print()
    
    def gauss(self):
        Q = []
        for i in range(5):
            Q.append([0]*6)
        E = self.ends
        for i in range(5):
            q,m,n =self.max1()
            print(q,m,n)
            for j in range(5):
                Q[m][j]=self.mat1[m][j]
            Q[m][5]=self.ends[m]
            for t in range(5):
                if(self.mat1[t][n]):
                    w = (-1)*(self.mat1[t][n])/q
                    print("w = ",w)
                    for p in range(5):
                        if self.mat1[t][p]==0:
                            p=p+1
                        else:
                            self.mat1[t][p]=self.mat1[t][p]+w*self.mat1[m][p]
                    self.ends[t]=self.ends[t]+w*self.ends[m]
            for k in range(5):
                self.mat1[m][k]=0
                self.mat1[k][n]=0
            print("A")
            self.printedmat(self.mat1)
            print("Q")
            self.printedmat(Q)
        
        print(E)
    
    
                    

        
def filling(a):
    a[0][0]=6.48
    a[0][1]=1.2
    a[0][2]=0.87
    a[0][3]=1.21
    a[0][4]=-0.06
    a[1][0]=1
    a[1][1]=3.94
    a[1][2]=1.3
    a[1][3]=-1.63
    a[1][4]=0.42
    a[2][0]=1.07
    a[2][1]=-2.46
    a[2][2]=5.66
    a[2][3]=2.1
    a[2][4]=0.883    
    a[3][0]=1.27
    a[3][1]=0.16
    a[3][2]=2.1
    a[3][3]=5.88
    a[3][4]=-10
    a[4][0]=0.54
    a[4][1]=-1.08
    a[4][2]=-0.617
    a[4][3]=5
    a[4][4]=-3

#prog
m = 5
a = []
for i in range(m):
    a.append([0]*m)
filling(a)
e = [2.1,0.24,2.15,6.44,-0.12]
print(a)
print(e)
Matrix = Matrix(a,e)
Matrix.gauss()