# Create Fibonacci list of 1000 elements.

fib = [0,1]
while len(fib) < 1000:
    fib.append(sum(fib[-2:])) # Sum of last two elements in list, a "slice".

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            n = int(line)
            print(fib.index(n))
