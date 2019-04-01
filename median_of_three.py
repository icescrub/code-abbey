data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        x = [map(int, line.split())] # Converts from list of strings to list of ints.
        x.sort()
        print(x[1])
