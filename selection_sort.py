def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
            line = [int(x) for x in data.read().split()] # Reads all data at once.

            for i in range(0,len(line)-1):
                if i == 0:
                    print(line.index(max(line)))
                    line[-1], line[line.index(max(line))] = max(line), line[-1]
                else:
                    print(line.index(max(line[:-i])))
                    line[-1-i], line[line.index(max(line[:-i]))] = max(line[:-i]), line[-1-i]
            print(line)
