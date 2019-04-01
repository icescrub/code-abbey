def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            w,h,L = [int(x) for x in line.split()]
            x,y = 0,0
            dx,dy = 1,1
            print(x,y)
            for i in range(100):
                x,y = stepx(x,w,L), stepy(y,h)
                print(x,y)

def stepx(x,w,L):
    global dx
    if x == 0:
        dx = 1
    elif x == (w - L):
        dx = -1
    return x + dx

def stepy(y,h):
    global dy
    if y == 0:
        dy = 1
    elif y == h - 1:
        dy = -1
    return y + dy
