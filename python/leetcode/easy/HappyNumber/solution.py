def isHappy(n: int) -> bool:
    res = True
    history = {}

    digits = intToDigits(n)
    temp = 0
    print(history)
    for digit in digits:
        temp += digit ** 2

    history[temp] = -1
    print(history)
    print(temp)
    while (temp != 1):
        digits = intToDigits(temp) 
        temp = 0
        for digit in digits:
            temp += digit ** 2

        if temp in history and temp != 1:
            print(temp)
            res = False
            break

        history[temp] = -1
        print(history)
                
    return res
    
def intToDigits(n: int) -> list[int]:
    strn = str(n)
    digits = [int(d) for d in strn]
    return digits
        
import sys

n = int(sys.argv[1])

result = isHappy(n)

print(result)
