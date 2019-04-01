data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        a = list(map(int,line.split()))
        for x in a[1:]:
            print(round((x-32)/1.8))
