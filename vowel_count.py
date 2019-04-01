data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def isVowel(string):
    return string.lower() in ['aeiouy'] # This accounts for upper cases.

def f(data):
    for line in data:
        x = map(isVowel,line)
        print(sum(x))
