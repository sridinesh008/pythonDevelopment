student= {'name':'Dinesh','Age':23,'courses':['Math','Physics']}
print("Getting the value using the key",student['name'],student['courses'])

#Use get to get no errror, it will the value or none 
print(student.get('name'),student.get('rollNo','not found'))

#Adding a value or updating a value

student['rollNo']='787-8978878'
student['name']='dinesh kumar'

print(student.get('name'),student.get('rollNo','not found'))

#using update method

student.update({'name':'S Dinesh kumar','Age':25.5})
print(student )


#Deleting a value

del student['rollNo']
print(student)

#Using Pop Method

popped_KeyValue=student.pop('Age')
print('After popping the value',student,'Popped value',popped_KeyValue)


'''Looping to  get or put a value from or to dictionary'''

student1={1:'Name',2:'Initial',3:'rollNo',4:['father\'s name','otherInfo']}
print(len(student1))
print(student1.keys())
print(student1.values())
print(student1.items())

for key1111,value in student1.items():
    print(key1111,value)




















