import math

def lcm(a,b):
    return abs(a*b)//math.gcd(a,b) if a and b else 0

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            x,y,N = [int(x) for x in line.split()]
            t = x*y*N/(x+y) # Wrong for whole numbers
            t_1 = max(x*math.floor(t/x), y*math.ceil(t/y))
            t_2 = max(x*math.ceil(t/x), y*math.floor(t/y))
            t = min(t_1,t_2)
            print(t)
