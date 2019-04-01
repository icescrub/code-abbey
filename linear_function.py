def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        mL, bL = [], []
        for line in data:
            p1x, p1y, p2x, p2y = [int(x) for x in line.split()]
            m = int((p2y - p1y)/(p2x - p1x))
            mL.append(m)
            b = int(p2y - m*p2x)
            bL.append(b)
            print('(' + str(m) + ' ' + str(b) + ')')
