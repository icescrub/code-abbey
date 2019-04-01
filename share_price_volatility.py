import statistics
# from statistics import stdev as std, mean as mu

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = line.split()
            company = line[0]
            prices = [int(x) for x in line[1:]]
            if statistics.stdev(prices) >= 0.04*statistics.mean(prices):
                print(company)
