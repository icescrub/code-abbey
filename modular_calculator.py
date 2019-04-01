data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f():
    x = int(data.readline())
    ax, bx = [],[]
    for line in data:
        a,b = line.split()
        ax.append(a)
        bx.append(int(b))
    mod = bx[-1]
#   mod = bx.pop() Returns last element, then removes it.
    ax = ax[:-1] # Removes last element of both arrays.
    bx = bx[:-1]
    for c,d in zip(ax,bx): # Iterates through tupled ("zipped") lists in parallel.
        global x
        if c == '*':
            x *= d
        else:
            x += d
        x %= mod
    print(x)
