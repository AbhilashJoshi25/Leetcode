#Notes

Binary Search: Divide the sorted array into 2 parts by finding the mid, check if the element exists in the left half or right half and return the index of the element found.

#Iterative
Binary search template:
Code implementation template:

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = left + ((right - left) // 2)
    if arr[mid] == target:
      #do something
      return
    if arr[mid] > target:
      right = mid - 1
    else:
      left = mid + 1

  # target is not in arr, but left is at insertion point
  return left
  -----------------------------------------------------------------------------
  def binary_search_recursive(arr, target, low, high):
    #base case for recursive
    if low > high:
      return -1
    mid = left + ((right - left) // 2)
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      return binary_search_recursive(arr, target, low, mid - 1)
    else:
      return binary_search_recursive(arr, target, mid + 1, high)
  -----------------------------------------------------------------------------