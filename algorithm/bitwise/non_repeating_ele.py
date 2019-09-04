"""
Find the two non-repeating elements in an array of repeating elements.
All the bits that are set in Xor will be set in one non-repeating element(x or y) and not in others. So if we take any
bit of xor and divide the elements of the array in two sets - one set of elements with same bit set and another set with
same bit not set. By doing so, we will get x in one set and y in another set. Now if we do Xor of all the elements in the
first set, we will get the first non-repeating element, and by doing same in other set we will get the second non-repeating
element.
"""


def get_2_non_repeating_ele(arr):
    set_bit_no = 0
    for i in arr:
        set_bit_no ^= i
    set_bit_no &= -set_bit_no
    x = y = 0
    for i in arr:
        if i & set_bit_no:
            x ^= i
        else:
            y ^= i
    return x, y


print(get_2_non_repeating_ele([1, 5, 2, 1, 7, 2, 9, 5]))
