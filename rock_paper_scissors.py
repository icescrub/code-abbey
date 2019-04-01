def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = line.replace('RR','0').replace('PP','0').replace('SS','0').replace('RP','-1').replace('RS','1').replace('PS','-1').replace('PR','1').replace('SR','-1').replace('SP','1')
            values = [int(x) for x in line.split()]
            print('1') if sum(values)>0 else print('2')
