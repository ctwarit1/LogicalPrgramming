"""
Given an integer array, in-place rearrange it such that it
 contains positive and negative numbers at alternate positions.
  Assume that all values in the array are non-zero.
• In case the multiple rearrangement exists, the solution can
return any one of them.
Input : [9, -3, 5, -2, -8, -6, 1, 3]
Output: [9, -3, 5, -2, 1, -8, 3, -6] or [5, -2, 9, -6, 1, -8, 3, -3]
or any other valid combination..
• If the array contains more positive or negative elements, the
solution should move them to the end of the array.
Input : [9, -3, 5, -2, -8, -6]
Output: [5, -2, 9, -6, -3, -8] or [-2, 5, -6, 9, -3, -8]
or any other valid combination..
Input : [5, 4, 6, -1, 3]
Output: [5, -1, 4, 6, 3] or [-1, 5, 4, 6, 3] or any other valid combination..
"""
list1 = [-1, -4, 9, 5]
new_list = []
# list1.sort()
for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] < 0:
            # new_list.append(list1[i])
            new_list.insert(0, list1[i])
        # if list1[j] < 0:
        #     new_list.append(list1[j])
        else:
            # new_list.append(list1[i])
            new_list.insert(0, list1[j])

print(new_list)
# for i in list1:
#     if i < 0 and list1.index(i) % 2 == 0:
#         list1.append(i)
#     else:
#         list1.append(i)
# print(list1)
