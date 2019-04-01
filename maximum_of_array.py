data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

maxD, minD = 0, 0

def f(data):
    for line in data:
        a = map(int,tuple(line.split()))
        for x in a:
            dataList.append(x)
        if maxD < max(dataList):
            maxD = max(dataList)
        elif minD > min(dataList):
            minD = min(dataList)
    print(maxD,minD)
