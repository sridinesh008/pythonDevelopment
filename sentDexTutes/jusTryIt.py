'''
Created on 23-Dec-2017

@author: sridi
'''
from _operator import index
from builtins import str

'''Try1'''
from _datetime import date, datetime

isRaining =True


while isRaining:
    #print("""IT is found raining at""",datetime.today())
    isRaining =False
exampleList = [1,2,3,4,5,6,7,8,9,10]    
'''Try2'''
def calledFunc():
    
    #print(len(exampleList))
    """for x in exampleList:
        print(x)"""
    for x in range(0,18):
        if (exampleList[x]%2)==0:
            print(x,exampleList[x])
            if index(exampleList[x])==len(exampleList):
                break;


'''try3'''
def task1():
    def task2():
        print('more tasks')


'''try3 lists'''

exampleList.append(78)
print(exampleList)
exampleList.insert(3, 'i\'m')
print(exampleList)
for values in exampleList:
    if type(values)==str:
        exampleList.remove(values)
exampleList.sort(reverse=True)
print(exampleList)


x = [[2,6],
     [6,2],
     [8,2],
     [5,12]
     ]
print(x[2][0])


