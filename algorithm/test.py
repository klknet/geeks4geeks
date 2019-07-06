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


def validateCode(code):
    check1 = (((ord(code[0]) + 3) << 1) + ((ord(code[1]) + 2) << 2) + ((ord(code[2]) + 1) << 3) + int(code[4], 16)) & 15
    check2 = (((ord(code[3]) + 3) << 1) + ((ord(code[6]) + 2) << 2) + ((ord(code[7]) + 1) << 3) + int(code[5], 16)) & 15
    check3 = (((ord(code[8]) + 3) << 1) + ((ord(code[9]) + 2) << 2) + ((ord(code[12]) + 1) << 3) + int(code[10],
                                                                                                       16)) & 15
    check4 = (((ord(code[13]) + 3) << 1) + ((ord(code[14]) + 2) << 2) + ((ord(code[15]) + 1) << 3) + int(code[11],
                                                                                                         16)) & 15
    return check1 == 0 and check2 == 0 and check3 == 0 and check4 == 0


def _ascii(c):
    v = int(c) if c.isdigit() else ord(c)
    return v


def swap_arr(arr):
    n = len(arr)
    i, j = 0, 0
    while i < n and j < n:
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] & 1 == 0:
            i += 1
        if arr[j] & 1 == 1:
            j += 1
    return arr


def swap_arr1(arr):
    n = len(arr)
    i, j = 0, n - 1
    while i < j:
        if arr[i] & 1 == 0:
            i += 1
            continue
        if arr[j] & 1 == 1:
            j -= 1
            continue
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


a = [1, 2, 3, 4, 5]
b = a[::2]
c = [x+1 for x in a]
a[::2] = [-1]*len(a[::2])
print(id(a), id(b), id(c))
print(a, b, c)

a = [1, 2, 3, 4, 5, 6, 7, 4, 8, 9]
a = [2, 1, 2, 1]
# print(swap_arr(a))
# print(swap_arr1(a))

c = ['0FYLIYY29P5A', 'A68E']
code = '0FYLA6IYY28E9P5A'
#
code = generateCode()
code = 'I0U00E34MYC8J3W8'
print(code)
valid = validateCode(code)
print(valid)
# print(uuid.uuid1())
# print(base64.b64encode('konglkqintian'.encode('utf8')))
