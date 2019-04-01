data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')


def f(data):
    for line in data:
        a,b = map(int,tuple(line.split()))
        print(min(a,b))
