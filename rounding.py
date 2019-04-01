data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        a,b = line.split()
        d = int(a)/int(b)
        if d%1 < 0.5:
            print(math.floor(d))
        else:
            print(math.ceil(d))
