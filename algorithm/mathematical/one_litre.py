"""
Measure one litre using two vessels and infinite water supply.
Let v1 be the vessel of capacity a and v2 be the capacity of b and a is smaller than b.
1)Do following while the amount of water of v1 is not 1.
...a)if v1 is empty, then completely fill v1.
...b)Transfer water from v1 to v2, if v2 becomes full, then keep remaining in v1 and empty v2.
2)v1 will have 1 litre after termination of loop in step 1, return.

Prove:
when v2 becomes full, we get
v1 = a - b*1 mod a in first time.
v1 = a - b*2 mod a in second time.
.
.
v1 = a - b*n mod a in n time.
We need to prove that the value of a-b*n mod a will be 1 after finite integer n.
For any co-prime integers a and b, exists a integer y such that b*y ≡ 1 mod a. After (a-1)*y iterations, we will have
a- [(a-1)*y*b] mod a water in v1, the value of this expression is a-[(a-1) mod a] which is 1. So the algorithm converges
and we get 1 litre in v1.
"""


def one_litre(a, b):
    a, b = min(a, b), max(a, b)
    v1, v2 = a, 0
    while v1 != 1:
        print('Vessel:', v1, 'Vessel2:', v2)
        v2 += v1
        if v2 > b:
            v1 = v2 - b
            v2 = 0
        else:
            v1 = a
    print('Vessel:', v1, 'Vessel2:', v2)


one_litre(107, 105)
