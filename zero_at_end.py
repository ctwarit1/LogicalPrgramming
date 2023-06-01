"""
Given an integer array, in-place move all zeros present
in it to the end. The solution should maintain the
relative order of items in the array and should not use constant space.
Input : [6, 0, 8, 2, 3, 0, 4, 0, 1]
Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]
"""
input = [6, 0, 8, 2, 3, 0, 4, 0, 1]
len_input = len(input)
count = 0
for i in input:
    if i == 0:
        count += 1
for i in range(len(count)):
    input.append(0)
print(input)
