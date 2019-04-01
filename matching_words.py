def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for line in data:
            line = [str(x) for x in line.split()][:-1]
            lineV = list(map(value,line)) # Value corresponding to line elements.
            lineM = []
            
            for i in lineV:
                lineM.append(0 if lineV.count(i) < 2 else 1)

            z = zip(line, lineV, lineM)
            f = [x for x in z if x[2] == 1] # List containing tuples of (word,val,count>1).
            words = []
            
            for x in f:
                global words
                words.append(x[0]) # Creates list of words with count > 1 "according to value".

            w2 = []
            for w in words:
                if words.count(w) > 1 and (w not in w2):
                    global w2
                    w2.append(w)
            w2.sort()
            final = ' '.join(w2)
            print(final)
                
            
#step1: create list of words from f.
#step2: for each word in list, count occurrences. if >1, print.
#step3: remove word from list using list comprehension.
            
def value(string):
    i = 0
    for c in string:
        i  += ord(c)
    return i
