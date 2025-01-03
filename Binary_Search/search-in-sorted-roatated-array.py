n=6
arr=[100, 200, 400, 1000, 10, 20]
x=10

#Function takes array and target element as input
def binary_search(arr, x):
  n = len(arr)
  low = 0
  high = n - 1
  #Binary search
  while low <= high:
    mid = left + ((right - left) // 2)
    if arr[mid] == x:
      return mid
    
    #First check if left half is sorted
    if arr[low]<=arr[mid]:
      #Check if the target element lies in the left half of array
      if arr[low] <= x <= arr[mid]:
        high = mid - 1
      else:
        low = mid + 1
    #Similarly check if right half is sorted
    if arr[mid] <= arr[high]:
      #check if the target element is in the right half of array
      if arr[mid] <= x <= arr[high]:
        low = mid + 1
      else:
        high = mid - 1
  return -1
    
