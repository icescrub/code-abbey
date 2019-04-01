# My original solution. Using deques in Python would make this significantly easier to reason about.

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            N,K = list(map(int,line.split())) # We assume N%K != 0, otherwise the problem is trivial.
            lstN = list(range(N))
            order = []
            i = 0
            
            while lstN:
                i = (K-1+i)%len(lstN)
                order.append(lstN.pop(i) + 1) # Extracts from one list, into another. +1 means 0 = 1st person, etc.

            print(order[-1])
