data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f():
    line1 = [int(x) for x in data.readline().split()]
    line2 = [int(x) for x in data.readline().split()]
    N, MAX = line1[0], line1[1]
    counter = [0]*MAX
    for i in range(0,N): # Fills in counter list.
        counter[line2[i]-1] += 1
    print(*counter, sep=' ')
