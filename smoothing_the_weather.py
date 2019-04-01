def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = [float(x) for x in line.split()]
            line2 = line.copy()
            for i in range(1,len(line2)-1):
                line2[i] = round((line[i-1] + line[i] + line[i+1])/3,7)
            print(line2)
