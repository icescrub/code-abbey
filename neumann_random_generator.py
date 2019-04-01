def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = list(int(x) for x in line.split())
            iterL = []
            for x in line:
                global iterL
                while iterL.count(x) < 2: # Makes sure sequence does not repeat.
                     iterL.append(x) if iterL == [] else None
                     x = (x**2//100)%10000 # Cuts off first, last 2 digits. This is called a "random step".
                     iterL.append(x)
                print(len(iterL) - 1)
                iterL.clear()
