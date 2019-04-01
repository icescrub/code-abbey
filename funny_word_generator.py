def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        _,X = [int(x) for x in data.readline().split()]
        line = [int(x) for x in data.readline().split()]
        consonants,vowels = 'bcdfghjklmnprstvwxz', 'aeiou'
        MC,MV = len(consonants),len(vowels)
        
        for length in line:
            x_new, X = LCG(length,X)
            
            string2 = ''
            for i,n in enumerate(x_new):
                if (i+1)%2:
                    string2 += consonants[n%MC]
                else:
                    string2 += vowels[n%MV]
            print(string2)

def LCG(length,X):
    A,C,M = 445,700001,2097152
    word = []
    for i in range(length):
        X = (A*X + C)%M
        word.append(X)
    return word,X
