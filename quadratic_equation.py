import math

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            A,B,C = [int(x) for x in line.split()]
            q(A,B,C)

def q(A,B,C):
    D = B**2 - 4*A*C

    if D == 0:
        R = -B//(2*A)
        print(R," ",R,end='; ')
    elif D > 0:
        TP = -B + math.sqrt(D)
        TN = -B - math.sqrt(D)
        LP = int(TP//(2*A))
        LN = int(TN//(2*A))
        MAX = max(LP,LN)
        MIN = min(LP,LN)
        print(MAX," ",MIN,end='; ')
    else:
        R = -B//(2*A)
        Lsafe = int(math.sqrt(abs(D))/(2*A))
        print(R,"+",Lsafe,"i ",sep='',end='')
        print(R,"-",Lsafe,"i",sep='',end='; ')
