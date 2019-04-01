from itertools import zip_longest

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            letters = [' ','t','n','s','r','d','!','c','m','g','b','v','k','q',\
                       'e','o','a','i','h','l','u','f','p','w','y','j','x','z']
            values = ['11','1001','10000','0101','01000','00101','001000',\
                      '000101','000011','0000100','0000010','00000001',\
                      '0000000001','000000000001','101','10001','011','01001',\
                      '0011','001001','00011','000100','0000101','0000011',\
                      '0000001','000000001','00000000001','000000000000']
            d = dict(zip(letters,values))

            converted_line = ''.join([d[s] for s in line])
            groups = grouper(converted_line,8,fillvalue = '0')
            hex_rep = [hex(int(''.join(g),2)) for g in groups]
            pretty_hex = [s[2:].upper().rjust(2,'0') for s in hex_rep]
            print(' '.join(pretty_hex))

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)
            
