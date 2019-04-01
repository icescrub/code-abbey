import math

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            fact = math.factorial # Function definition.

            N,K = [int(x) for x in line.split()]
            if N == K:
                print(1)
            elif K == 0:
                print(1)
            else:
                M = max(K,N-K)
                P = min(K,N-K)
                lstP = list(range(1,P+1))
                NUM = list(set(range(1,N+1))^set(range(1,M+1)))
                print(multL(NUM)//multL(lstP))

def multL(lst):
    y = 1
    for x in lst:
        global y
        y *= x
    return y if lst else 0
