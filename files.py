#Python has functions for creating, reading, updating and deleting files.

#Open a file
from os import write


myFile=open('myFile.txt', 'w')

#Get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)


#Write to file
myFile.write('I love python')
myFile.write(' and Javascript')
myFile.close()

print('Is closed: ', myFile.closed)

#Append to file
myFile=open('myFile.txt', 'a')
myFile.write(' and I also like PHP')

#Read from file
myFile=open('myFile.txt', 'r+')
text=myFile.read(100)
print(text)