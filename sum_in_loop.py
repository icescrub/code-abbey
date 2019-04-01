data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    a = map(int,tuple(data.read().split()))
    return sum(a)
