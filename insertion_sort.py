def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        line = [int(x) for x in data.readline().split()]

        for i in range(1,len(line)):
            j = i-1
            pivot = line[i]
            shift = 0
            while (line[j] > pivot) and (j >= 0):
                line[j+1] = line[j]
                shift += 1
                j -= 1
            line[j+1] = pivot
            print(shift)
