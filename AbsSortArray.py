def absSort(arr):
  #sorted(arr) #your code goes here
  #print(sorted(arr))
  #abs1= arr[0];
  #for i in range(len(arr)):
  #  for j in range(len(arr)-1): 
  #    if (abs(arr[j]) > abs(arr[j+1])) or (abs(arr[j]) == abs(arr[j+1]) and (arr[j+1] <0)) :
  #      arr[j] , arr[j+1] = arr[j+1] , arr[j]     
  #return arr
  return sorted(arr, key=lessThan)


def lessThan(x):
  if x < 0:
    return abs(x) - 0.5
  return x
