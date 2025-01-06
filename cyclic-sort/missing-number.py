'''
Cyclic sort is a simple and efficient in-place sorting algorithm used for sorting arrays with integers in a specific range, most of the time [1 – n]. 
It places each element in its correct position by iteratively swapping it with the element at the position where it should be located. This process continues until all elements are in their proper places, resulting in a sorted array.

But how do we know the correct position of any element? This is where the algorithm makes things even easier: the correct place of any element is simply the value of element - 1. For example, if we have the array [3,1,2], then the correct position of the first element, 
(3−1) th index, i.e., index 2 and not 0. Similarly, the correct position for the elements 1 and 2 is index 0 and 1, respectively.

e.g:   0, 1, 2, 3, 4, 5 => Indexes
arr = [2, 6, 4, 3, 1, 5]
o/p arr = [1, 2, 3, 4, 5]
'''
def find_missing_number(nums):
  len_nums = len(nums)
  index = 0

  while index < len_nums:
    value = nums[index]

    if value < len_nums and value != nums[value]:
      nums[index], nums[value] = nums[value], nums[index]

    else:
      index += 1

  for x in range(len_nums):
    if x != nums[x]:
      return x
  return len_nums
