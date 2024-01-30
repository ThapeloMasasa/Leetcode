# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
def isBadVersion(num):
    pass

def firstBadVersion(nums):
    pt1 = 0
    pt2 = len(nums) - 1

    while pt1 < pt2 - 1:
        mid = (pt1 + pt2) // 2
        if  isBadVersion(mid):
            pt2 = mid 
        else:
            pt1 = mid
    return pt2
