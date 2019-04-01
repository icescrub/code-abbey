def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            X, N = [int(x) for x in line.split()]
            r = 1
            for i in range(N):
                r = (r + X/r)/2
            print(r)
                
                
