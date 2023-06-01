"""
Given two sorted integer arrays `X[]` and `Y[]` of size `m` and `n`
each where `m >= n` and `X[]` has exactly `n` vacant cells,
merge elements of `Y[]` in their correct position in array `X[]`,
i.e., merge `(X, Y)` by keeping the sorted order.
Input : Two arrays X[] and Y[] where vacant cells in X[] is represented by 0.
X[] = [0, 2, 0, 3, 0, 5, 6, 0, 0]
Y[] = [1, 8, 9, 10, 15]
Output: X[] = [1, 2, 3, 5, 6, 8, 9, 10, 15]
"""


def merge_array(x, y):
    for i in x:
        for j in y:
            if i == 0:
                x.remove(i)
                x.insert(0, j)

    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
    print(x)


# merge_array([0, 2, 0, 3, 0, 5, 6, 0, 0], [1, 8, 9, 10, 15])
# merge_array([0, 30, 0, 60, 50, 0, 0], [10, 70, 40, 20])

"""
Given two sorted integer arrays, `X[]` and `Y[]` of size `m` and `n` each
, in-place merge elements of `X[]` with elements of array `Y[]` by 
maintaining the sorted order, i.e., fill `X[]` with the first `m` smallest 
elements and fill `Y[]` with remaining elements.
Input :
X[] = [1, 4, 7, 8, 10]
Y[] = [2, 3, 9]
Output:
X[] = [1, 2, 3, 4, 7]
Y[] = [8, 9, 10]
"""


def merge_sorted_arrays(list1, list2):
    i = len(list1) - 1
    j = len(list2) - 1
    while i >= 0 and j >= 0:
        if list1[i] > list2[j]:
            list1[i + j + 1] = list1[i]
            i -= 1
        else:
            list1[i + j + 1] = list2[j]
            j -= 1
    while j >= 0:
        list1[j] = list2[j]
        j -= 1
    return list1, list2


print(merge_sorted_arrays([1, 4, 7, 8, 10], [2, 3, 9]))
