def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = [int(x) for x in line.split()]
            
            # 32 = ' ', 46 = '.', 65-89 = A..Z, 97-122 = 'a..z'
            acceptable = [32,46]+list(range(65,91))+list(range(97,123))
            mask = 0b01111111 # Eliminates most significant bit.

            # Filters corrupted bytes (odd bits).
            line2 = list(filter(lambda x: binString(x).count('1')%2 == 0,line))
            
            message = ''
            for x in line2:
                if x in acceptable:
                    message += chr(x)
                else:
                    message += chr(x&mask)
            print(message)

def binString(b):
    x_b = []
    i = 0
    for i in range(7,-1,-1):
        global x_b
        if b&(1<<i) != 0:
            x_b.append('1')
        else:
            x_b.append('0')
    return x_b
