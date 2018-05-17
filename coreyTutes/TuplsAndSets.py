'''
Created on 16-Dec-2017

@author: sridi

'''


'''Empty list,Tuple,Set'''

empty_list=[]
empty_list=list()

empty_tuple=()
empty_tuple=tuple()

empty_set={}#This is wrong actual is below
empty_set=set()


'''Tuples'''
#Mutable
list_1=['Course0','Course1','Course3','Course4']
list_2=list_1
print(list_1,list_2)

list_1[0]='courses'
print(list_1,list_2)

#immutable

tuple_1=('Course0','Course1','Course3','Course4')
tuple_2=tuple_1
print(tuple_1,tuple_2)
#tuple_1[0]='Course0'
#print(tuple_1,tuple_2)


'''Sets-Automatically remove duplicates'''
set_1={'Course0','Course1','Course3','Course4','Course0'}
print("Watch deplicates removed",set_1)
print("As sts ar optimized for finding a value lets do it",'Course0' in set_1)

#intersection & difference
set_1={1,2,3,4,5}
set_2={4,5,6,7,8}
print("Values exist in both sets are:",set_1.intersection(set_2))
print("Values does not exist in both sets are:",set_1.difference(set_2))
print("Getting all the values in two sets:",set_1.union(set_2))









