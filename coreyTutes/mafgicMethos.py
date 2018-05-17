'''
Created on 17-Dec-2017

@author: sridi
'''
class EmployeeDetails:
        
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        
    def fullName(self):
        return '{} {} '.format(self.first,self.last)
    
    def __repr__(self):
        return "EmployeeDetails('{}', '{}', {})".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return '{} -  {}'.format(self.fullName(),self.email)
             
    def __add__(self,other):
        return self.pay+other.pay
    def __len__(self):
        return len(self.fullName())     
     
        
emp1=EmployeeDetails('dinesh','kumar',90000)
emp2=EmployeeDetails('dinesh1','kumar1',70000)

print(len('test')) 

print(len(emp1))

#print(repr(emp1))
#print(str(emp1))

#print(int.__add__(1,2))