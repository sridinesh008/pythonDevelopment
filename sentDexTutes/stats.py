'''
Created on 24-Dec-2017

@author: sridi
'''
import statistics

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]


y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)