data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    a,b = map(int,data.read().split())
    return a+b
