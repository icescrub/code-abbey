def f():
    with open('C:\\Users\\Duchess\\Desktop\\Data.txt') as data:
        for line in data:
            line2 = list(filter(lambda x: isBracket(x), line)) # Filters out non-brackets.
            i = 0
            
            while i+1 < len(line2): # if all pairwise elements don't match, this condition fails.
                global i
                if isMatch(line2[i],line2[i+1]):
                    del line2[i] # Deletes first matching bracket, shifting list down 1.
                    del line2[i] # Deletes second matching bracket, now in i-th position.
                    i = 0
                else:
                    i += 1
            print('0') if len(line2) else print('1')

def isBracket(character):
    bracket = ['[', ']', '(',')', '{', '}', '<', '>']
    return character in bracket

def isMatch(char1,char2):
    if (char1 == '(' and char2 == ')'):
        return True
    elif (char1 == '[' and char2 == ']'):
        return True
    elif (char1 == '{' and char2 == '}'):
        return True
    elif (char1 == '<' and char2 == '>'):
        return True
    else:
        return False
