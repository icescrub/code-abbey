def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for line in data:
            word = str(line)
            wordALNUM = ''.join([c for c in word.lower() if c in alphabet]) # Takes out symbols and converts to lowercase to identify equality.
            print('Y') if wordALNUM == wordALNUM[::-1] else print('N')
