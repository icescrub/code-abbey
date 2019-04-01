def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            rot, word = line.split()
            rot = int(rot)
            lst = [c for c in word] # Manipulate string as list, which is easier.
                
            if rot < 0:
                lst.reverse()
                rotateString(rot,lst)
                lst.reverse()
            else:
                rotateString(rot,lst)

            rStr = ''.join(lst)
            print(rStr)

def rotateString(rot,lst): # Append first char to end, then delete first char.
    for i in range(abs(rot)):
        lst.append(lst[0])
        del(lst[0])

