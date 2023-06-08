def selection_sort():
    """selection sorting"""

    a = [38, 52, 9, 18, 6, 13, 63]
    for i in range(len(a)):
        min_value = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_value]:
                min_value = j
        temp = a[i]
        a[i] = a[min_value]
        a[min_value] = temp
    for i in range(len(a)):
        print(a[i])


print("------------> Selection sorting")
selection_sort()


# def sort_string(s):
#     chars = list(s)
#     n = len(chars)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if chars[j] > chars[j+1]:
#                 chars[j]= chars[j+1]
#                 chars[j+1] = chars[j]
#     return ''.join(chars)
# s = "geekforgeeks"
# print("Original string:", s)
# print("String after sorting:", sort_string(s))

def bubble_sort(a):
    """Bubble sorting"""

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    for i in range(len(a)):
        print(a[i])


print("------------> Bubble sorting")
bubble_sort([38, 52, 9, 18, 6, 13, 63])


def insertion_sort(a):
    """Insertion sorting"""

    for i in range(len(a)):
        temp = a[i]
        j = i

        while j > 0 and a[j - 1] > temp:
            a[j] = a[j - 1]
            j = j - 1

        a[j] = temp

    for i in range(len(a)):
        print(a[i])


print("------------> Insertion sorting", )
insertion_sort([38, 52, 9, 18, 6, 13, 63])


def quick_sort(lst):
    """Quick sorting"""

    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    smaller, equal, larger = [], [], []

    for num in lst:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    smaller = quick_sort(smaller)
    larger = quick_sort(larger)

    return smaller + equal + larger


print("------------> Quick sorting\n", quick_sort([4, 2, 7, 1, 5, 3]))


def merge_sort(lst):
    """Merge sort"""
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


print("------------> Merge sorting\n", merge_sort([4, 2, 7, 1, 5, 3]))
print("------------> Merge sorting of string\n", merge_sort("twarit"))


def bubble_sort_string(s):
    li = list(s)
    for i in range(len(li)):
        for j in range(0, len(li) - 1):
            if li[j] > li[j + 1]:
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp
    return ''.join(li)


s = "twarit"
print("------------> bubble sorting of string\n", bubble_sort_string(s))
