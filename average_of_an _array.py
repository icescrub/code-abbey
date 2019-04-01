data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        a = list(map(int,line.split())) # Splits string into array of integers.
        a = a[:-1] # Remove last number.
        xbar = round(sum(a)/len(a))
        print(xbar)
