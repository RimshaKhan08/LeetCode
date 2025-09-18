def remove_dup(arr):
    k = 0
    i = 0
    while i < len(arr):
      j = i + 1
      while j < len(arr):
         if arr[j] == arr[i]:
            arr.pop(j)
            k+=1   
         else:
            j += 1
      i += 1

    return (arr , k)

arr = [1,1,2,2,3,3,4,4,5,5]
print(remove_dup(arr))

