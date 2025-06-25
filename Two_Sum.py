"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
def twoSum(nums, target):

    for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]

#Array of integers
nums = [2,7,11,15]

#Target integer
target = 9

#Print result of twoSum function
print(twoSum(nums, target))

#[0,1] = expected output for nums = [2,7,11,15] and target = 9