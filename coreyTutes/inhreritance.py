'''
Created on 17-Dec-2017

@author: sridi
'''

class EmployeeDetails:
    raise_Amt=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        
    def fullName(self):
        return '{} {} '.format(self.first,self.last)
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_Amt)
 
class developer(EmployeeDetails):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) # or  EmployeeDetails.__init__(self,first,last,pay)
        self.prog_lang=prog_lang   

class manager(EmployeeDetails):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay) # or  EmployeeDetails.__init__(self,first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=[employees]
         
    def add_employee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)
            
    def remove_employee(self,employee):
        if employee in self.employees:
            self.employees.remove(employee) 

    def print_employee(self):
        for employee in self.employees:
            print('--->',super().fullName())
            

        
dev1=developer('dinesh','kumar',90000,'java')
dev2=developer('dinesh1','kumar1',70000,'python')
dev3=developer('dds','kumar1',70000,'python')

mngr1= manager('good','managr',100000,[dev1])

mngr1.add_employee(dev3)
#mngr1.add_employee(dev3])

mngr1.print_employee()

#mngr1.print_employee()
#print(help(developer))
#print(dev1.email,dev2.prog_lang)

#print(dev1.pay)
#dev1.apply_raise()
#print(dev1.pay)