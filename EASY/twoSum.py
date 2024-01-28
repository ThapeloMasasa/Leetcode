# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    store = {}
    for i in range(len(nums)):
        complement = abs(target - nums[i])
        if nums[i] in store:
            ans = [i, store[nums[i]]]
            return ans
        else:
            store[complement] = i
    print(store)

#test cases
#test1
arr1 = [2,4,6,8,3,9]
target1 = 14
ans1 = twoSum(arr1, target1)
print(ans1)
#test2
arr2 = [3,6,1,5,3,7]
target2 = 10
ans2 = twoSum(arr2, target2)
print(ans2)
