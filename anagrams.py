data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')
dictionary = open('C:\\Users\\Duchess\\Desktop\\words.txt')

def f():
    dictSorted = [sorted(list(x)) for x in dictionary]
    for word in data:
        wordSorted = sorted(list(word))
        print(dictSorted.count(wordSorted)-1)
