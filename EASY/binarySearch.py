# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def binarySearch(nums, target):
    pt1 = 0
    pt2 = len(nums) - 1
    while pt1 <= pt2:
        mid = (pt1 + pt2) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > target:
            pt2 = mid - 1
        else:
            pt1 = mid + 1
    return False

#tests
#test1
nums = [1,2,3,4,5,6,7,8]
target = 4
ans = binarySearch(nums, target)
print(ans)

