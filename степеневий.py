import numpy as np

def iter(A,r,v,i=1,e=0.00001):
    rk=np.matmul(A,r)
    v1=np.divide(rk,r)
    if((abs(v1[0][0]-v[0][0])<e)): #and abs(v1[0][1]-v[0][1])<e) and (abs(v1[0][2]-v[0][2])<e and abs(v1[0][3]-v[0][3])<e)):
        print("\n\nІтераційний процес завершено!!!")
        print("iter ",i)
        #print("A:\n",A)
        print("Власний вектор:\n",rk)
        print("Власне число = ",(v1[0][0]+v1[1][0]+v1[2][0]+v1[3][0])/4)
        print("Вектор нев'язки:\n",abs(v1-v))
        return 
    else:
        print("iter ",i)
        #print("A:\n",A)
        print("Власний вектор:\n",rk)
        print("Власне число = ",(v1[0][0]+v1[1][0]+v1[2][0]+v1[3][0])/4)
        print("Вектор нев'язки:\n ",abs(v1-v))
        return iter(A,rk,v1,i+1)
#start
A = np.array([[6.48,1.2,0.87,1.21],
             [1.2,3.94,1.3,0.16],
             [0.87,1.3,5.66,2.1],
             [1.21,0.16,2.1,5.88]])
r = np.array([[1],[1],[1],[1]])
v=np.array([[0],[0],[0],[0]])
iter(A,r,v)