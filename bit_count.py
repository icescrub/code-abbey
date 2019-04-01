# My original solution. The superior solution is further below.

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            list = [int(x) for x in line.split()]
            binR = ''
            for y in list:
                global binR
                binR = ''
                for i in range(32):
                    global binR
                    if y&2**i:
                        binR += '1'
                print(len(binR))
                    
"""
The canonical "counting set bits" solution. Much closer to the metal.
def count_bits(x):
    c = 0
    for i in range(32):
        c += (x & 1)
        x >>= 1
    return c
"""
