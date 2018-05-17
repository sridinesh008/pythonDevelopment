'''
Created on 16-Dec-2017

@author: sridi
'''
from _ast import Num

#Type prediction 
num=3
print(type(num))
num=3.14
print(type(num))
num ="fsafs"
print(type(num))

##Arithmetic Operators

print(9+5,"Addition")
print(9-5,"minus")
print(9*5,"Mulitiplication")
print(9/5,"Division")
print(9//5,"Floor division")
print(9**5,"Exponents")
print(9%5,"Modular")


#Increment

num =1
num = num+1
print(num) #THis is same as  below

num =1 
num+=1 #This can be used with other ops too
print(num)

num=25
num *=5
print(num)

num=25
num /=5
print(num)

'''Absolute Values'''

Num = -3 
print("Abs Val=",abs(Num))
Num= 3
print("Abs Val=",abs(Num))
Num =435435.6824
print("Abs Val=",abs(Num),"Round Value",round(Num,1),"Round Value",round(Num)) 
'''Syntax= ROUND(value to be rounded , at\
which decimal point it should be rounded)'''

Num= -2342/234
print("Abs Val=",abs(Num))


'''Comparison operators'''
num_1=3
num_2=2

print(num_1==num_2)
print(num_1!=num_2)
print(num_1<num_2)
print(num_1>num_2)
print(num_1<=num_2)
print(num_1>=num_2)


'''TypeCasting'''
num_1='2121'
num_2='213'
print("Before Casting",num_1+num_2)

num_1=int('2121')
num_2=float('213')
print("After Casting",num_1+num_2)





