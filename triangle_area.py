import math

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            x1,y1,x2,y2,x3,y3 = map(int, line.split())
            a = math.sqrt((x2-x3)**2 + (y2 - y3)**2)
            b = math.sqrt((x1-x3)**2 + (y1 - y3)**2)
            c = math.sqrt((x1-x2)**2 + (y1 - y2)**2)
            s = (a + b + c)/2
            A = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print(A)
