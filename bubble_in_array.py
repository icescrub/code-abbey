swaps = 0

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = list(int(x) for x in line.split())
            line = line[:-1]
            for i in range(len(line)):
                if i == len(line) - 1:
                    break
                if line[i] > line[i+1]:
                   line[i+1], line[i] = line[i], line[i+1]
                    global swaps
                    swaps += 1
            print(swaps,checksum(line))

def checksum(arr):
    result = 0
    for x in arr:
        global result
        result = (113*(result+x))%10000007
    return result
