data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        a = list(map(int,line.split())) # Splits string into array of integers.
        A,B,N = a
        print(int(N*(A + (N-1)*B/2))) # Produced error when I used integer division. Be careful about this in the future.
