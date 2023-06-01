"""
Given an unsorted integer array, find all pairs with
a given difference `k` in it using constant space.
Input : nums = [1, 5, 2, 2, 2, 5, 5, 4], k = 3
Output: {(2, 5), (1, 4)}
Note:
• The solution should return the pair in sorted order.
For instance, among pairs (5, 2) and (2, 5), only pair (2, 5) appeared in the output.
• Since the input can contain multiple pairs with a given
difference, the solution should return a set containing all
the distinct pairs. For instance, the pair (2, 5) appeared only once in the output.
"""
nums = [1, 5, 2, 2, 2, 5, 5, 4]
new_num = sorted(nums, reverse=True)
visit = []
for i in range(len(new_num)):
    visit.append(False)

k = 3
final_list = []
print(new_num)
for i in range(len(nums)-1):
    cur_list = []
    if visit[i] == True:
        continue
    else:
        for j in range(i+1, len(nums)):
            visit[i] = True

            if nums[i] - nums[j] == k:
                cur_list.append(nums[i])
                cur_list.append(nums[j])
    final_list.append(cur_list)
print(final_list)


# Output: {(2, 5), (1, 4)}