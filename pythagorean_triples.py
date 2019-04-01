def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            n = int(line)
            for a in range(1,n):
                if (n*n-2*n*a)%(2*n-2*a) == 0:
                    b = (n*n-2*n*a)//(2*n-2*a)
                    print((n-a-b)**2)
                    break
