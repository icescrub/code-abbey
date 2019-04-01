"""
d1 = v1*t, d2 = v2*t
v2 is negative (going opposite direction), so d2 = -v2*t
d1 is constructed as 0, so d2 = d1 + d
Thus, when the distances are equivalent, they meet. v1*t - d = -v2*t
t = d/(v1+v2)
The distance from d1 is v1*t = v1*d/(v1+v2)
"""

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            d,v1,v2 = list(map(int,line.split()))
            print(d*v1/(v1+v2))
