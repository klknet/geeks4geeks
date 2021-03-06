"""
Babylonian method for square root.
1. Start with an arbitrary positive start value x(the closer to the root, the better)
2. Initialize y = 1.
3. Do following util desired approximation is achieved.
    a)Get the next approximation for root using average x and y.
    b)Set y=n/x.
"""


def binary_square_root(n):
    low, high = 0, n
    e = 0.000000001
    count = 0
    while abs(high-low) > e:
        count += 1
        m = (high+low)/2
        cur = m*m
        if cur > n:
            high = m
        elif cur < n:
            low = m
        else:
            print('bin', count)
            return m
    print('bin', count)
    return high


def baby_square_root(n):
    p = 1
    q = n
    e = 0.000000001
    count = 0
    while abs(q-p) > e:
        count += 1
        p = (p+q)/2
        q = n/p
    print('baby', count)
    return p


n = 500
print(binary_square_root(n))
print(baby_square_root(n))