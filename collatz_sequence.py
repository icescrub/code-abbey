# My original solution. Further below is the solution that matches the definition of the Collatz Sequence.

data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f():
    line = [int(x) for x in data.readline().split()]

    for x in line:
        count = 0
        while x != 1:
            if x%2:
                x = 3*x + 1
            else:
                x /= 2
            count += 1
        print(count)
        count = 0

"""
This definition is easier to read, being more in line with the definition of the Collatz Sequence.

def collatzCount(num):
    if num == 1:
        return 0
    elif num % 2 == 0:
        return 1 + collatzCount(num / 2)
    else:
        return 1 + collatzCount(3*num + 1)
