s1, s2, dt, listDT = 0, 0, 0, []

def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line = [int(x) for x in line.split()]
            list1, list2 = line[:4][::-1], line[4:][::-1] # list1 = t1, list2 = t2 (t2>t1), reversed lists (s m h d)
            listS = [1,60,3600,86400]
            
            for x,y in list(zip(list1,listS)): # Find t1 in seconds.
                global s1
                s1 += x*y

            for x,y in list(zip(list2,listS)): # Find t2 in seconds.
                global s2
                s2 += x*y

            dt = s2 - s1
            
            #for x in listS[::-1]: # 1 60 3600 86400
            for i in range(len(listS)): # 0 --> 3
                global listDT
                listDT.append(dt//listS[len(listS)-1-i]) # Adds correct d/h/m/s to list.
                dt %= listS[len(listS)-1-i] # Decreases time remaining after extracting d/h/m/s.
            print(" ".join(str(x) for x in listDT))

            # Clear all variables for next loop.

            global s1, s2, dt, listDT
            s1 = 0
            s2 = 0
            dt = 0
            listDT.clear()
