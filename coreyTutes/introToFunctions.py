'''
Created on 16-Dec-2017

@author: sridi
'''
def emptyFunc():
    pass
print(emptyFunc())



def first_func():
    print("Its my first def")
first_func()



def firstReturn():
    return """returning value"""
print(firstReturn().capitalize())


def firstParameterized(greeting,name='you'):
    return '{} to the function {} !'.format(greeting,name)
print(firstParameterized('welcome').capitalize())
print(firstParameterized('welcome','Dinesh').capitalize())


#args & kwargs

def studentInfo(*args,**kwargs):
    print(args)
    print(kwargs)
studentInfo('math','art',name='dinesh',age=22)
coursez=['math','art']
info={'name': 'dinesh', 'age': 22}
studentInfo(coursez,info)
studentInfo(*coursez,**info)

"""One small progsram"""
#no of days as per month, first value is placeholder for indexing purpose

month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap(year):
    """return true for leap * flase for non - leap"""
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    """"return number of days in a month in that year"""
    
    if not 1 <= month <=12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]


print(days_in_month(8000, 2))
print(days_in_month(2017, 2))
