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


def bubble_sort():
    """Bubble sorting"""

    a = [38, 52, 9, 18, 6, 13, 63]
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    for i in range(len(a)):
        print(a[i])


print("------------> Bubble sorting")
bubble_sort()


def insertion_sort():
    """Insertion sorting"""

    a = [38, 52, 9, 18, 6, 13, 63]
    for i in range(len(a)):
        temp = a[i]
        j = i

        while j > 0 and a[j - 1] > temp:
            a[j] = a[j - 1]
            j = j - 1

        a[j] = temp

    for i in range(len(a)):
        print(a[i])


print("------------> Insertion sorting")
insertion_sort()


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
