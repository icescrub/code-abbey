# My original solution. Superior solution further below.

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shift = 0
        line2 = ''
        
        for line in data:
            if line[0].isdecimal():
                global shift
                line = line.split()
                shift = 26 - int(line[1])
                print(shift)
            else:
                global shift
                global alphabet
                global line2
                
                for i in range(len(line)):
                    if line[i].isalpha():
                        line2 += alphabet[(alphabet.index(line[i]) + shift)%26]
                    else:
                        line2 += line[i]
            print(line2)
            line2 = ''

"""
Much better solution uses dictionary to correlate letter with shifted letter. Other solutions use chr() and ord() functions.

import string
letters = string.ascii_uppercase

intro = [int(x) for x in input().split()]
times, shift = intro

cipher = {letters[(letters.index(x) + shift) % 26] : x for x in letters}
cipher[' '] = ' '
cipher['.'] = '.'

for _ in range(times):
    ciphertext = input()
    res = ""
    for i in ciphertext:
        res += cipher[i]
    print(res, ' ')
