'''
Created on 16-Dec-2017

@author: sridi
'''


'''LISTS'''

courses=['Maths','Testing','C++']

#Finding Length
print("Length of the list is ",len(courses))

#Finding a value using index
print("The 2nd value is ",courses[1])
print("The last value using negative index",courses[-1])

#Slicing
print("SLice method 1",courses[0:2])
print("SLice method 2",courses[-2:-1])
print("SLice method 3",courses[:])
print("SLice method 4",courses[0:])
print("SLice method 5",courses[:2])

#Adding a value to List
courses.append('Physics')
print("After Append",courses)
courses.insert(10, 'StudyInsert')
print("After Insertion",courses)

courses_2=['ARts','Sci']

courses.insert(0,courses_2)
print("AFter inserting a list to list",courses)
courses.remove(['ARts', 'Sci'])
print("After Removing, using a value",courses)
popped=courses.pop()
print("After Removing, using pop",courses,"Popped value is",popped)
courses.extend(courses_2)
print("AFter Extending a list with list",courses)

#Sorting a list
courses.reverse()
print("Using reverse",courses)
courses.sort()
print("Simple sort",courses)

num=[13,2312,124142424,4214242,242424]
num.sort(key=None, reverse=False)
print("Simple sort",num)

num.sort(key=None, reverse=True)
print("Desc sort",num)

sorted_courses=sorted(courses)
print("SOrted list vafiable",sorted_courses)


#min,max,num
print("Minimum value",min(num))
print("MAx value",max(num))
print("Sum of the list",sum(num))


#Find Index
print("Getting index using value ",courses.index('C++'))
print("Finding the existence, if the value is exist then it returns ",'C++' in courses)

#For loop

for index,course in enumerate(courses,start=3):
    print(index,course)
    

course_str=', '.
print("GEtting aSTring from a list comma separated",course_str)




