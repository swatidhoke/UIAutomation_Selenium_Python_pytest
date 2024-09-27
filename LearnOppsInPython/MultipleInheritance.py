
'''
This is example of multiple intertance
'''
class A:
     #class varible 
    varA = 'welcome to class A'
class B:
    varB = "welcome to class B"
class C(A, B):
    varC = "welcome to class C"
     
print(C.varA)
print(C.varB)
print(C.varC)

