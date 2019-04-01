def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            S,R,P = list(map(int,line.split()))
            count = 0
            
            while S < R:
                S *= round((1+P/100),2)
                count += 1

            print(count)
