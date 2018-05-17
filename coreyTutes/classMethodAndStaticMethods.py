'''
Created on 17-Dec-2017

@author: sridi
'''
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
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay= emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday()== 6:
            return False
        return True
emp1=EmployeeDetails('dinesh','kumar',90000)
emp2=EmployeeDetails('dinesh1','kumar1',70000)

EmployeeDetails.set_raise_amt(1.05)
print(EmployeeDetails.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

emp_str_1='New1-emp1-1000'
emp_str_2='New2-emp2-2000'
emp_str_3='New3-emp3-3000'


new_emp1=EmployeeDetails.from_string(emp_str_1)

print(new_emp1.fullName())

import datetime

my_date = datetime.date(2017,12,25)

print(EmployeeDetails.is_working_day(my_date))