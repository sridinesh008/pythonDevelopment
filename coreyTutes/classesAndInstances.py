'''
Created on 12-Dec-2017

@author: sridi
'''
#import antigravity

class Employee:
    pass

class EmployeeDetails:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        
    def fullName(self):
        return '{} {} '.format(self.first,self.last)
        
emp1=EmployeeDetails('dinesh','kumar',90000)
emp2=EmployeeDetails('dinesh1','kumar1',70000)


#print(emp1,emp2)

print(emp1.email,emp2.email)
print(emp1.fullName(),EmployeeDetails.fullName(emp1))



