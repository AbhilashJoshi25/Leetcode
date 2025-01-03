#Binary Search
##Problem Statement
'''You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000'''

##Solution Summary
'''We calculate the mid index by adding the Left and Right pointers and dividing the result by 2. 
This is the middle of our search space.

L - the left-most index of the current subarray.
R - the right-most index of the current array.
mid - L + R / 2, the index at which the current sub-array divides itself into two equal halves.

#Imp point:
A better formula for calculating the mid value is L + (R - L) / 2. This will prevent any potential integer overflow errors. This article from Google Research provides an intuitive explanation.'''

##Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            #(l + r) // 2 can lead to overflow

            mid = left + ((right - left) // 2)

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return - 1
