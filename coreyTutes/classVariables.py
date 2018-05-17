'''
Created on 15-Dec-2017

@author: sridi
'''
'''
Created on 12-Dec-2017

@author: sridi
'''
#import antigravity

class Employee:
    pass

class EmployeeDetails:
    numOfEmps=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        EmployeeDetails.numOfEmps +=1
    def fullName(self):
        return '{} {} '.format(self.first,self.last)
      
    def apply_rais(self):
        self.pay=int(self.pay*self.raise_amt)
        return self.pay  


print(EmployeeDetails.numOfEmps)
emp1=EmployeeDetails('dinesh','kumar',90000)
emp2=EmployeeDetails('dinesh1','kumar1',70000)
print(EmployeeDetails.numOfEmps)
print(emp1.pay)
print(emp1.apply_rais())
print(EmployeeDetails.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)


