def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for x in data:
            x = int(x)

            primes = list(sieve(10000))
            factors = []

            for p in primes:
                while x%p == 0:
                    factors.append(p)
                    x //= p
            
            print('*'.join([str(f) for f in factors]))

def sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
        multiples.update(range(i*i, n+1, i))
