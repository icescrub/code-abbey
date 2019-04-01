def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            d1,d2 = map(int, line.split())
            N = 6

            print((d1%N + 1) + (d2%N + 1))
