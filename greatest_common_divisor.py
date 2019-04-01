# My original solution. Faster and better solution further below.

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            a,b = map(int,line.split())
            print('(%d %d) '%(gcd(a,b),lcm(a,b)))

def gcd(x,y):
    while((x!=0) & (y!=0)):
        if x > y:
            x = x%y
        else:
            y = y%x
    return max(x,y)

def lcm(x,y):
    return x*y//gcd(x,y)

"""
Better solution.

def gcd(x,y):
    while y:
        x, y = y, x%y
    return x
