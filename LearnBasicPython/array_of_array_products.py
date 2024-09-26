def array_of_array_products(arr):
  n = len(arr);
  if (n == 0) or (n ==1):
        # nothing to multiply if n equals to 0 or 1
    return []
  productArr = []
  for i in range(n):
    product =1
    for j in range(n):
       if(i != j):
          product *= arr[j]
    productArr.append(product)
  return(productArr)


test_arr = [8, 10, 2]
print(array_of_array_products(test_arr))
