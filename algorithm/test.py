import random
import string


def generateCode():
    baseCode = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))
    print(baseCode)
    checkBit = [format((16 - (((ord(baseCode[n]) + 3) << 1) + ((ord(baseCode[n + 1]) + 2) << 2) + (
                (ord(baseCode[n + 2]) + 1) << 3))) & 15, 'x').upper() for n in range(0, 10, 3)]
    print(checkBit)
    finalCode = list(baseCode)
    finalCode.insert(4, checkBit[0])
    finalCode.insert(5, checkBit[1])
    finalCode.insert(10, checkBit[2])
    finalCode.insert(11, checkBit[3])
    return ''.join(finalCode)


print(generateCode())
