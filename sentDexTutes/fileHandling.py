'''
Created on 24-Dec-2017

@author: sridi
'''
"""creating&writing a file """
text = "sample text to save \nnew line !"

# notifies Python that you are opening this file, with the intention to write
#writing will clear the file and write to it just the data you specify in the write operation. 

savefile=open('exampleFile.txt','w')

# actually writes the information
savefile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
savefile.close()

'''appending a file'''

# so here, generally it can be a good idea to start with a newline, since
# otherwise it will append data on the same line as the file left off.
# you might want that, but I'll use a new line.
# another option used is to first append just a simple newline
# then append what you want. 
appendNames = '\nDinesh\nKumar\nMurali\nSridhar'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendNames)
appendFile.close()
#What will happen here is, if exampleFile.txt already exists, the appendMe line will be added to it. 
#If that file does not already exist, then it will be created.
# this will instead read the file into a python list. 
readMe = open('exampleFile.txt','r').readlines()
print(readMe)
