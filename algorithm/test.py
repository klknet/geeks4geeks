import random
import string
import uuid
import base64


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


a= [1, 2, 3, 4, 5, 6, 7, 4, 8, 9]
a = [2, 1, 2, 1]
# print(swap_arr(a))
print(swap_arr1(a))

# print(generateCode())
# print(uuid.uuid1())
# print(base64.b64encode('konglkqintian'.encode('utf8')))
