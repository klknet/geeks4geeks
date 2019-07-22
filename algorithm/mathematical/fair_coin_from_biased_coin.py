"""
Make a fair coin from a biased coin.
We know foo() returns 0 with 60% probability. How can we ensure that 0 and 1 are returned with 50% probability?
If we somehow get two cases with equal probability, then we are done. We call foo two times. Both calls will return 0 with
60% probability. So the two pairs (0,1) and (1,0）will be generated with equal probability from two calls of foo. Let us
see how.
(0,1): The probability to get 0 followed by 1 from two calls of foo() = 0.6*0.4=0.24
(1,0): The probability to get 1 followed by 0 from two calls of foo() = 0.4*0.6=0.24
So the two cases appear with equal probability. The idea is to return consider only the above two cases, return 0 in one
case, return 1 in other case. For other cases, recur until you end up in any of the above two cases.
"""
import random


def fair_coin():
    first = foo()
    second = foo()
    if first + second == 1:
        return first == 0
    return fair_coin()


def foo():
    r = random.random()
    if r < 0.4:
        return 1
    else:
        return 0


def coin_trail():
    trueCount = 0
    falseCount = 0
    for i in range(100):
        v = fair_coin()
        if v:
            trueCount += 1
        elif not v:
            falseCount += 1
    return trueCount / falseCount


sample = 10000
trail = []
for i in range(sample):
    trail.append(coin_trail())
print(sum(trail) / sample)
