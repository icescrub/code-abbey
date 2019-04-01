def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        primes = list(sieve(3000000))
        for line in data:
            L,R = [int(x) for x in line.split()]
            iR = primes.index(R)
            iL = primes.index(L)
            i = iR - iL + 1
            print(i)

def sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
        multiples.update(range(i*i, n+1, i))
