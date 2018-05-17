'''
Created on 17-Dec-2017

@author: sridi
'''
import datetime

from classMethodAndStaticMethods.EmployeeDetails import is_working_day
my_date = datetime.date(2017,12,25)

print(is_working_day(my_date))