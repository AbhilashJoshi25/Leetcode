'''🧠Intuition
Cyclic Sort: Correct position of any element is element value - 1

➡️Approach
check if the curr ele is in correct position in array with range [1, n] and is at correct position
swap the curr ele to its correct position
iterate through the array again and check if each element is equal to its index plus 1
Complexity
Time complexity: O(N)
Space complexity: O(1)'''
#©️Code
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Cyclic sort algorithm says correct position of any element is element value - 1
        # [3, 1, 2] => correct position of 3 in a sorted array will be  3 - 1 = 2nd index of [1, 2, 3] as its 0-indexed

        index = 0

        while index < len(nums):
            correct_position = nums[index] - 1

            # check if the curr ele is in correct position in array with range [1, n] and is at correct position
            if 0 <= correct_position < len(nums) and nums[index] != nums[correct_position]:
                #swap the curr ele to its correct position
                nums[index], nums[correct_position] = nums[correct_position], nums[index]
            else:
                index += 1
        
        # iterate through the array again and check if each element is equal to its index plus 1
        for x in range(len(nums)):
            if x + 1 != nums[x]:
                return x + 1
        return len(nums) + 1 
