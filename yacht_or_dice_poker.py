def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = [int(x) for x in line.split()]

            y = [0]*6
            for i in range(1,7):
                y[i-1] = line.count(i)

            if y.count(2) == 1 and y.count(3) == 0:
                print("pair")
            elif y.count(3) == 1 and y.count(2) == 0:
                print("three")
            elif y.count(4) == 1:
                print("four")
            elif y.count(5) == 1:
                print("yacht")
            elif y.count(2) == 2:
                print("two-pairs")
            elif y.count(3) == 1 and y.count(2) == 1:
                print("full-house")
            elif sorted(line) == [1,2,3,4,5]:
                print("small-straight")
            elif sorted(line) == [2,3,4,5,6]:
                print("big-straight")
            else:
                print("none")
