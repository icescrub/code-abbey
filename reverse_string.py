data = open('C:\\Users\\Duchess\\Desktop\\Data.txt')

def f():
    line = list(data.read()) # Read as a string.
    n = len(line)
    for x in range(0,n//2): # Swap first and last characters, moving inward.
        line[x], line[n-x-1] = line[n-x-1], line[x]
    reverse = ''
    for x in line: # Take array of characters, make it a string.
        reverse += x
    # ''.join(line) # This is the common way of doing that conversion.
    print(reverse)
    # print(input()[::-1]) This is the easy way of doing it.
