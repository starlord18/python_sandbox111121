#Adictionary is a collection which is unorderd, changeable and indexed. No duplicate numbers.


#create dict
person = {
    'first_name' :'Wasim',
    'last_name' : 'Akhtar',
    'age' : 21
}

print(person, type(person))


#use constructor
#person2 = dict(first_name = 'Sara', last_name = 'Williams', age = 23)

#print(person2, type(person2))

#get value
print(person['first_name'])
#print(person2.get('last_name'))

#Add key/value
person['phone'] = '555-5555-555'

print(person)


#get dict keys
print(person.keys())

#get dict items
print(person.items())

print(person)

#copy dict
person2 = person.copy()

person2['city'] = 'Boston'

print(person2)


#Remove item
del(person['age'])
person.pop('phone')

print(person)

#clear
person.clear()

#Get Length
print(len(person2))

print(person)


#List of dict
people = [
    {'name' : 'Martha', 'age' : 30},
    {'name' : 'Kevin', 'age' : 25}
]

print(people[1]['name'])