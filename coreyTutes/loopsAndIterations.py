'''
Created on 16-Dec-2017

@author: sridi
'''

#Simple for loop
num =[1,2,3,4,5,6,7,8]

for nums in num:
    if nums==1 or nums == 4:
        print("Expected data found",nums)
        continue
    print(nums)
    if nums==7:
        print("Expected data found",nums)
        break 
    print(nums)

#nested for loop

for nums in num:
    for letters in 'abc':
        for items in ['item1']:
            print(nums,letters,items)


#Range

for i in range(10):
    print(i)
    for i in range(2,5):
        print(i)
        
#While loop

x = 4
while x<10:
    print(" x is a lesser value",x)
    #x += 1
    if x>5:
        break
            
