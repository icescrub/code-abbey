data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')


def f(data):
    for line in data:
        a = map(int,tuple(line.split()))
        print(min(a))
