def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        x, guesses = data.readline().split()
        xs = str(x)
        xset = set(xs)
        lst = [str(x) for x in data.readline().split()]
        lstset = [set(x) for x in lst]

        correctT1 = []
        correctT2 = []
        for x in lst:
            correct = ''
            for i in range(len(xs)):
                if xs[i] == x[i]:
                    correct += '1'
            correctT1.append(len(correct))
            total = len(set(xs)&set(x))
            correctT2.append(total - len(correct))

        for x in list(zip(correctT1,correctT2)):
            print("{}-{}".format(x[0],x[1]))
