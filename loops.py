#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string)

people = ['John', 'Sara', 'Paul', 'Susan']

#Simple for loop
for person in people:
    print(f'Current person :{person}')
    
    
#break
for person in people:
    if person == 'Paul':
        break
    print(f'Current person :{person}')
    
    
#continue
for person in people:
    if person == 'Paul':
        continue
    print(f'Current person :{person}')
    
    
#range
for i in range(len(people)):
    print(people[i])
    

for i in range(0,11):
    print(f'Number : {i}')





#while loops execute a set of statements as long as a condition is true.

count =0
while count<=10:
    print(f'Count : {count}')
    count +=1