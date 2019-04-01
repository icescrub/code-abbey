# NOTE: This solution has been surpassed by more efficient solutions in other file sets.

swaps, passes = 0, 0

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = list(int(x) for x in line.split())
            while (notOrdered(line)):
                for i in range(len(line)):
                    if i == len(line) - 1:
                        global passes
                        passes += 1
                    elif line[i] > line[i+1]:
                        temp = line[i+1]
                        line[i+1] = line[i]
                        line[i] = temp
                        global swaps
                        swaps += 1
            global passes
            passes += 1
            print(passes, swaps)

def notOrdered(lst):
    diffList = list(zip(lst,lst[1:]))
    ordered = [1 if i-j <= 0 else 0 for i,j in diffList]
    return not all(ordered)
