import math

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            P,R,L = [int(x) for x in line.split()]
            r = (1 + (R/12)*(1/100))
            f = r**L/((r**L - 1)/(r-1)) # Uses arithmetic series.
            M = f*P
            print(math.ceil(M))
