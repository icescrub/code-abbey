data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        a = list(map(int,line.split())) # Splits string into array of integers.
        for x in a:
            D = list(zip(str(x),range(1,len(str(a))+1))) # Packages number with its position via zip, which is then converted to a list.
            E = 0
            for x,y in D:
                E += int(x)*y # Multiplies tuple elements as requested in PS.
            print(E)
