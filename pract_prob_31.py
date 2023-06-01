"""
Create a function which takes a list of integers lst
and a positive integer k and returns the minimum and
maximum possible product of k elements taken from the
list. If enough elements are not available in the list, return None.
Examples
product_pair([1, -2, -3, 4, 6, 7], 1) ➞ (-3, 7)
product_pair([1, -2, -3, 4, 6, 7], 2) ➞ (-21, 42)
# -3*7, 6*7
product_pair([1, -2, -3, 4, 6, 7], 3) ➞ (-126, 168)
# -3*6*7, 4*6*7
product_pair([1, -2, -3, 4, 6, 7], 7) ➞ None
# There are only 6 elements in the list
"""

"""
def product_pair(lst, k):
    if k >= len(lst):
        return None
    else:
        lst.sort()
        if k == 1:
            min_product = lst[0]
            max_product = lst[-1]
            return min_product, max_product
            
        min_lst = lst[-(k-1):]
        print(min_lst)
        min_product = 1 * lst[0]
        
        for i in range(len(min_lst)):
            min_product *= min_lst[i]
        max_lst = lst[-k:]
        max_product = 1
        
        for j in range(len(max_lst)):
            max_product *= max_lst[j]
        return min_product, max_product
"""



def product_pair(list1, x):
    list1 = sorted(list1)                              # [-3, -2, 1, 4, 6, 7]
    min = 1
    max = 1
    if len(list1) < x:
        print(None)
    else:
        for i in range(x):
            min *= list1[i]
            max *= list1[-1 - i]
            # min *= list1[-1-i]
        print(min, max)


product_pair([1, -2, -3, 4, 6, 7], 1)  # Output: (-3, 7)
product_pair([1, -2, -3, 4, 6, 7], 2)  # Output: (-21, 42)
product_pair([1, -2, -3, 4, 6, 7], 3)  # Output: (-126, 168)
product_pair([1, -2, -3, 4, 6, 7], 7)  # Output: None
