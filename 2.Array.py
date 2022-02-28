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
