import math
from math import tan as T, pi as P

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            D,B = [float(x) for x in line.split()]
            H = D*T(P*(B-90)/180)
            print(round(H))
