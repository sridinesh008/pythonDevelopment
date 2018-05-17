'''
Created on 16-Dec-2017

@author: sridi
'''

#Object identity: is
lang='python'

if lang=='python':
    print("lang matched")
elif lang=='java':
    print('lang is java')
else:
    print("lang does not matched")

#And,OR,NOT

version=2
langIsEasy=True

if lang=='python' and version>=3 and langIsEasy:
    print("Correct version & language")
elif lang=="python" or version<3 and langIsEasy:
    print("Correct version or language")
if not langIsEasy:
    print("Lang is not easy")
else:
    print("It is easy")
    


#Object Identity : is

a = [1,2,3]
b=[1,2,3]
print("A equals B ",a==b)
print(id(a),id(b))
print("A is B ",a is b)
c=[1,2,3]
b=c 
print("C equals B ",c==b)
print(id(c),id(b))
print("C is B ",c is b)



#False Vales
   #false
   #None
   #Zero of any numeric
   #Any empty sequence , for eg., '' , () , [].
   #Any empty mapping , for rg ., {}.

condition = False

if condition:
    print("It is true")
else:
    print("It is false")
    
condition = None

if condition:
    print("It is true")
else:
    print("It is false")
    
condition = 0
if condition:
    print("It is true")
else:
    print("It is false")

condition = 10
if condition:
    print("It is true")
else:
    print("It is false")
    
condition = []

if condition:
    print("It is true")
else:
    print("It is false")

condition = ''

if condition:
    print("It is true")
else:
    print("It is false")
    
condition = ()

if condition:
    print("It is true")
else:
    print("It is false")
    
condition = {}

if condition:
    print("It is true")
else:
    print("It is false")
    
condition = {1:'someValue'}

if condition:
    print("It is true")
else:
    print("It is false")


















