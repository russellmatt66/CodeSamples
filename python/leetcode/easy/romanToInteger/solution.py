def romCharToInt(c: chr) -> int:
    if(c == 'I'):
        return 1
    elif(c == 'V'):
        return 5
    elif(c == 'X'):
        return 10
    elif(c == 'L'):
        return 50
    elif(c == 'C'):
        return 100
    elif(c == 'D'):
        return 500
    elif(c == 'M'):
        return 1000
    else:
        print('input is not a Roman numeral')
        return -1
    
def needToSub(currChr: chr, nextChr: chr) -> bool:
    if(currChr == 'I' and (nextChr == 'V' or nextChr == 'X')):
        return True
    elif(currChr == 'X' and (nextChr == 'L' or nextChr == 'C')):
        return True
    elif(currChr == 'C' and (nextChr == 'D' or nextChr == 'M')):
        return True
    else:
        return False
    
class Solution:
    def romanToInt(self, s: str) -> int:
        nmrlidx = 0
        nmrlSum = 0
        while(nmrlidx < len(s)):
            currInt = romCharToInt(s[nmrlidx]) # convert current character
            if (nmrlidx == len(s) - 1): # last character, just need to add
                return nmrlSum + currInt
            elif(needToSub(s[nmrlidx],s[nmrlidx+1])):
                nmrlSum -= currInt
            else: # don't need to subtract
                nmrlSum += currInt
            nmrlidx += 1