data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        a = [int(x) for x in line.split()]
        result = 0
        for x in a:
            result = (113*(result+x))%10000007 # seed = 113, limit = 10000007
        print(result)
