def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        line = [int(x) for x in data.readline().split()]
        for M in line:
            print(fibmod(10000,M)[1:].index(0,1)+ 1)

def fibmod(n,M): # Creates Fibonacci list, modulated, with n elements.
    fibmod = [0,1]
    while len(fibmod) < n:
        fibmod.append((fibmod[-1] + fibmod[-2])%M)
    return fibmod
