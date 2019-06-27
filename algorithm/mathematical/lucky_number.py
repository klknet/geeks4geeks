"""
Lucky numbers are subset of integers.
Take the set of integers.
1,2,3,4,5,6,7,8,9
First, delete every second number, we get following reduced set.
1,3,5,7,9
Now, delete every third number, we get
1,7,9
Continue this process indefinitely...
Any number that does not deleted due to above process is called 'lucky'.

Before every iteration, if we calculate position of the given no, then in a given iteration, we can determine if the
no will be deleted. Suppose calculated position of given no. is p before some iteration, and each ith no. will be removed
in this iteration, if P < i then input no. is lucky, if P is such that P%i==0(i is divisor of P), then input no. is not
lucky.
"""


def isLucky(n):
    if n < isLucky.counter:
        return 1
    if n % isLucky.counter == 0:
        return 0
    n -= n // isLucky.counter
    isLucky.counter += 1
    return isLucky(n)


isLucky.counter = 2
print(isLucky(19))
