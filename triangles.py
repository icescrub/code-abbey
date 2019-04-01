data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        a = list(map(int,line.split())) # Splits string into array of integers.
        a.sort()
        a1,a2,a3 = a
        print(int(not (a1+a2)<a3 ))
        # A triangle can be built if, for all sides, a+b>=c.
        # A triangle cannot be built if there exists one side s.t. a+b<c.
