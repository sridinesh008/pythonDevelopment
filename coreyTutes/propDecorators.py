'''
Created on 17-Dec-2017

@author: sridi
'''
class EmployeeDetails:
        
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property  
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
    
    @property
    def fullName(self):
        return '{} {} '.format(self.first,self.last)
    
    @fullName.setter
    def fullName(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
    @fullName.deleter
    def fullName(self):
        print("Delete Name!")
        self.first=None
        self.last=None   
    
emp1=EmployeeDetails('dinesh','kumar')

emp1.fullName='murali dinesh'

del emp1.fullName

print(emp1.first)
print(emp1.fullName)
print(emp1.email)
