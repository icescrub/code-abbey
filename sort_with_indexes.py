def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = list(int(x) for x in line.split())

            dict = {}

            for i,j in enumerate(line): # i=position,j=line[i]
                dict[j] = i+1
                
          # for i in range(len(line)):
              # dict[line[i]] = i+1


            line.sort()
          # line = sorted(line)

            for x in line:
                print(dict[x])
