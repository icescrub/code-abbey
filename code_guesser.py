def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        
        # Creates initial numbers.
        q = set(str(i).zfill(4) for i in range(10000))
        
        for line in data:
            x,n = [int(x) for x in line.split()]
            num = str(x).zfill(4)
            
            # Filters for any values that may work.
            q = set(filter(lambda x: matching(x,num) == n,q))

        # Print answer.
        print(int(list(q)[0]))

def matching(x,y):
	return sum([1 for i in range(4) if x[i] == y[i]])
