 # Top 10 Array Functions in Python

# Python Built-in List Functions:
# 1. len(list) - Returns the number of elements in the list.
#    Example: len([1, 2, 3]) returns 3.
#
# 2. list.append(item) - Adds an item to the end of the list.
#    Example: [1, 2].append(3) results in [1, 2, 3].
#
# 3. list.extend(iterable) - Extends the list by appending elements from an iterable.
#    Example: [1, 2].extend([3, 4]) results in [1, 2, 3, 4].
#
# 4. list.insert(index, item) - Inserts an item at a specified index.
#    Example: [1, 2].insert(1, 3) results in [1, 3, 2].
#
# 5. list.remove(item) - Removes the first occurrence of an item from the list.
#    Example: [1, 2, 2].remove(2) results in [1, 2].
#
# 6. list.pop(index) - Removes and returns the item at the specified index (or the last item if index is not provided).
#    Example: [1, 2, 3].pop(1) returns 2 and results in [1, 3].
#
# 7. list.sort(key=None, reverse=False) - Sorts the list in place.
#    Example: [3, 1, 2].sort() results in [1, 2, 3].
#
# 8. list.reverse() - Reverses the elements of the list in place.
#    Example: [1, 2, 3].reverse() results in [3, 2, 1].
#
# 9. list.count(item) - Returns the number of occurrences of an item in the list.
#    Example: [1, 2, 2].count(2) returns 2.
#
# 10. list.index(item) - Returns the index of the first occurrence of an item in the list.
#     Example: [1, 2, 3].index(2) returns 1.

# NumPy Array Functions:
# 1. numpy.array() - Creates an array from a list or tuple.
#    Example: numpy.array([1, 2, 3]) returns array([1, 2, 3]).
#
# 2. numpy.arange(start, stop, step) - Creates an array with values from start to stop (exclusive) with a specified step.
#    Example: numpy.arange(0, 10, 2) returns array([0, 2, 4, 6, 8]).
#
# 3. numpy.linspace(start, stop, num) - Creates an array with num evenly spaced values from start to stop.
#    Example: numpy.linspace(0, 1, 5) returns array([0. , 0.25, 0.5 , 0.75, 1. ]).
#
# 4. numpy.reshape(array, new_shape) - Reshapes the array to the specified shape.
#    Example: numpy.array([1, 2, 3, 4]).reshape((2, 2)) returns array([[1, 2], [3, 4]]).
#
# 5. numpy.flatten() - Flattens a multi-dimensional array into a 1D array.
#    Example: numpy.array([[1, 2], [3, 4]]).flatten() returns array([1, 2, 3, 4]).
#
# 6. numpy.sum(array, axis=None) - Computes the sum of array elements along a specified axis.
#    Example: numpy.array([[1, 2], [3, 4]]).sum() returns 10.
#
# 7. numpy.mean(array, axis=None) - Computes the mean of array elements along a specified axis.
#    Example: numpy.array([1, 2, 3, 4]).mean() returns 2.5.
#
# 8. numpy.max(array, axis=None) - Returns the maximum value of the array along a specified axis.
#    Example: numpy.array([1, 2, 3, 4]).max() returns 4.
#
# 9. numpy.min(array, axis=None) - Returns the minimum value of the array along a specified axis.
#    Example: numpy.array([1, 2, 3, 4]).min() returns 1.
#
# 10. numpy.transpose(array) - Permutes the dimensions of the array.
#     Example: numpy.array([[1, 2], [3, 4]]).transpose() returns array([[1, 3], [2, 4]]).


# 1-->Print an Array and index of an aaray
def print_array(arr):
    for i in range(1,len(arr)):
        print(i, arr [i])
  
#2--> Print Say Hello
def say_hello():
    print('Hello, World')

#3--> #while and if else
def print_if_large(x):   
    if x>20:
        print(x);
    else:
        print("Try a bigger num");
        
 #4--> Print multiple varible in one line     
def printmultiple():
#Many Values to Multiple Variables
    x, y, z = "Orange", "Banana", "Cherry"
    print(x,y,z)

 #5-->Check Prime Number
def primenumber(num):
# define a flag variable
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


#6--> Write a python program to print fibonaci series:
def fibonaci(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0
# check if the number of terms is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    # generate fibonacci sequence
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1

#7--> Python Program to Check if a Number is Positive, Negative or 0    
def pos_neg(num):
    if num == 0 :
        print("zero")
    elif num >0 :
        print("greater");
    else :
        print("smaller");
        
#8-->Check if a Number is Odd or Even
def even_odd(num):
    if num%2 ==0 :
        print("{0} is Even".format(num))
    else:
        print("{0} is odd".format(num))  
        
#9-->Print list in reverse
test_Lst = [12, 5, 7, 8, 9]
def reverselist(Lst):
    #Sort the list
    Lst.sort()
    #Reverse the list
    print(Lst[:: -1])

#10-->print if string is palindrom
def palindrome(test_str):
    print(test_str);
    rev_test_str ="".join(reversed(test_str)) ;
    if test_str == rev_test_str :
        print ("isPlaindrome")
    else :
        print ("isNotPlaindrome")
        
#11-->Print number of words in a given sentence
def numofwords(s):
    print(len(s.split()))
   
     
print_if_large(3)
printmultiple()
primenumber(4)
fibonaci(7)
pos_neg(3)
even_odd(3)
reverselist(test_Lst)
palindrome("tet")
numofwords("My name is Swati")
