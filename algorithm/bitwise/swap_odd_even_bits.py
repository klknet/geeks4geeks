"""
Swap all odd and even bits.
If we take a closer look at the example, we can observe that we basically need to right shift all even bits, and left
shift all odd bits by 1.
1)Get all even bits of x by doing bitwise and of x with 0xAAAAAAAA. The number 0xAAAAAAAA is a 32 bit number with all
even bits set as 1 and odd bits as 0.
2)Get all odd bits of x by doing bitwise and of x with 0x55555555. The number of 0x55555555 is a 32 bit number with all
even bits set as 0 and odd bits as1.
3)Right shift all even bits and Left shift all odd bits.
4)Combine all even bits and odd bits and return.
"""


def swap(n):
    even_bits = (n & 0xAAAAAAAA) >> 1
    odd_bits = (n & 0x55555555) << 1
    return even_bits | odd_bits


print(swap(23))
