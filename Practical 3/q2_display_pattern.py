# Displaying patterns
# by Yiyang, 04/02/18

# main ideas: 
# build a string of 'n n-1 n-2 ... 2 1' first
# print it by line, and use the space between num. in the str to see if the num. shld be printed or replaced by ' '

def building_pattern(n):
    
# WRONG METHOD:
#   numStr = ""
#    for i in range(n):
#        numstr = str(i+1) + " " + numStr
    
    strList = []
    for i in range(n):
        strList.append(str(n-i))
        
        if i != n-1:
            strList.append(' ')
    
    return ''.join(strList)
    
def display_pattern(n):
    
    numStr = building_pattern(n)
    _len = len(numStr)
    
    # printing
    for i in range(n):
        count = 0       # count the num. of ' ' read to see if the current num shld be printed
        for j in range(_len):
            if count + i < n - 1:
                print(' ', end='')
            else:
                print(numStr[j], end='')
            
            if numStr[j] == ' ':
                count += 1
        print()          # to start a new line
        
    return

patternSize = int(input())
display_pattern(patternSize)