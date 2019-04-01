import itertools, statistics
from itertools import islice
from statistics import mean as mu

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        line = [int(x) for x in data.read().split()]
        lists = []
        splits = [-1] + [i for i,x in enumerate(line) if x == 0]
        indices = n_grams(splits,2)
        for i,j in indices:
            lists.append(line[i+1:j])

        # These are the core metrics for each data set.
        metrics = [(s_range(range(x,x*y+1)),\
                    max(range(x,x*y+1)),\
                    mu(range(x,x*y+1))) \
                   for x in [1,2,3,4,5] for y in [2,4,6,8,10,12]]
        
        dice = ["1d2","1d4","1d6","1d8","1d10","1d12",\
                "2d2","2d4","2d6","2d8","2d10","2d12",\
                "3d2","3d4","3d6","3d8","3d10","3d12",\
                "4d2","4d4","4d6","4d8","4d10","4d12",\
                "5d2","5d4","5d6","5d8","5d10","5d12"]

        # Dice rolls corresponding to core metrics.
        d = dict(zip(metrics,dice))
        
        # Now in the same format as the metrics.
        values = [(s_range(r),max(r),mu(r)) for r in lists]

        d1 = [(distance(values[0],m),m) for m in metrics]
        d2 = [(distance(values[1],m),m) for m in metrics]
        d3 = [(distance(values[2],m),m) for m in metrics]
        
        print(d[min(d1,key=lambda x:x[0])[1]])
        print(d[min(d2,key=lambda x:x[0])[1]])
        print(d[min(d3,key=lambda x:x[0])[1]])

        #distance = [abs(r-m) for r,m in zip(values,]
        #print(d[answer(values[0],metrics)])
        
        
        #print(d[answer(lists[0],metrics)])
        #print(d[answer(lists[1],metrics)])
        #print(d[answer(lists[2],metrics)])

# These functions are copied from the Python documentation.

def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)

def s_range(lst):
    return max(lst) - min(lst)

def answer(lst,lst2):
    g = {distance(x,r):r for x in lst for r in lst2}
    return g[min(g)]

def distance(r,m):
    return sum([abs(i-j) for i,j in zip(r,m)])
