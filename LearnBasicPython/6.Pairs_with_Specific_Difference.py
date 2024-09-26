def find_pairs_with_given_difference(arr, k):
  num_map = {}
  output_arr = []

  for x in arr:
    num_map[x-k] = x
    
  for y in arr:
    if y in num_map:
      output_arr.append([num_map[y], y])
         
  return output_arr;
  
test_input = [0, -1, -2, 2, 1]
k =1
find_pairs_with_given_difference(test_input , k)
