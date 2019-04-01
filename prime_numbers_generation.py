def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        primes = list(sieve(3000000))
        for line in data:
            line = [int(x) for x in line.split()]
            for x in line:
                print(primes[x-1])

def sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
        multiples.update(range(i*i, n+1, i))
