'''
Basically a strobogrammatic number is a number which looks same after 180 degree rotation.
Example: 808, 69, 101, etc

Problem statement:
246. Strobogrammatic Number

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
 

Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.

Intuition
Initialize a dictionary with numbers and their corresponding rotations

Approach
Use 2 ptrs to traverse from left and right inwards, checking each element in the string is having a corresponding rotated digit match in the strobogrammatic dictionary

Complexity
Time complexity: O(N) as we traverse through the whole string 'num'
Space complexity: O(1) as we have fixed size strobogrammatic dictionary
'''

class solution:
  def isStrobogrammatic(self, num: str) -> bool:
    left = 0
    right = len(num) - 1
    #Initialize a dictionary that contains corresponding rotated numbers
    s_dict = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    while left <= right:
      if num[left] not in s_dict or s_dict[num[left]] != num[right]:
        return False
      left += 1
      right -= 1
    return True
