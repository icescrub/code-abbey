import math

data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f(data):
    for line in data:
        x = list(map(int, line.split()))
        y = x[0]*x[1] + x[2]
        log_y = math.ceil(math.log10(y)) # Tells us how many times we'll need to mod it.
        ynum = []
      # for _ in range(0,log_y): Can also just use blank instead of i.
        for i in range(0,log_y):
            global y, ynum
            ynum = ynum + [y%10]
            y //= 10
        print(sum(ynum))
    #   Alternative: use ynum += y%10 and print(ynum) rather than arrays.
