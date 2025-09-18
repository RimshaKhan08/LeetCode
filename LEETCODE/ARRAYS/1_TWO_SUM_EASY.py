def two_Sum(nums, target):
        for i in range(len(nums)):
           for j in range(1, len(nums)):
               if (nums[i] + nums[j]) == target:
                  return(i, j)
        else: 
          return[]

arr = [2,7,11,15]
print(two_Sum(arr, 9))

arr = [3,2,4]
print(two_Sum(arr, 6))

        

