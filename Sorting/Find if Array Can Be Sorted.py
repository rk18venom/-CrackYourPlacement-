#Link: https://leetcode.com/problems/find-if-array-can-be-sorted/description/?envType=daily-question&envId=2024-11-06

#Solution
def setbit(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def canSortArray(nums):
    n = len(nums)
    
    # Iterate and only swap adjacent elements with the same set bit count if needed
    for i in range(n - 1):
        for j in range(n - i- 1):
            if nums[j] > nums[j + 1] and setbit(nums[j]) == setbit(nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    # Check if the array is sorted
    return nums == sorted(nums)

#Main
t=int(input())
while t!=0:
    num=[int(x) for x in input().split()]
    print(canSortArray(num))  # Output: True or False
    t-=1
    