def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line2 = [int(x)**2 for x in line.split()]
            print(sum(line2))
