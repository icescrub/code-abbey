import math

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            C = [float(x) for x in line.split()]

            L,R,d = 0,100,1
            while d > 1E-7:
                global R
                gL = g(L,C)
                gR = g(R,C)
                M = (L + R)/2
                gM = g(M,C)
                if gM >= 0:
                    R = M
                else:
                    L = M
                d = R - L

            print(L)

# Note: g is monotonic, so binary search may be used to find x = 0.

def g(x,C):
    return C[0]*x + C[1]*x**(3/2) - C[2]*math.exp(-x/50) - C[3]
