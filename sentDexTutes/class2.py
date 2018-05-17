'''
Created on 23-Dec-2017

@author: sridi
'''
from jusTryIt import calledFunc


#calledFunc()
def simple_addition(num1,num2=7):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

simple_addition(3,3)


# this variable has no parent function, but is actually NOT a global variable.
# it just so happens that it is committed to memory before the function is called
# so we are able to iterate, or call it out, but we cannot do much else.

x = 6

def example():
    print(x)
    # z, however, is a local variable.  
    z = 5
    # this works
    print(z)
    
example()
# this does not, which often confuses people, because z has been defined
# and successfully even was called... the problem is that it is a local
# variable only, and you are attempting to access it globally.

print(x)

