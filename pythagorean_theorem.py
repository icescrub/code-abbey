def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            A, B, C = list(map(int,line.split()))

            if C**2 > (A**2 + B**2):
                print('O')
            elif C**2 < (A**2 + B**2):
                print('A')
            else:
                print('R')
