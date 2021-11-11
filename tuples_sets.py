#A tuple is a collection which is ordered and unchangeable. Allows duplicate numbers

#create tuples
fruits=('Apples', 'Pears', 'Chikoo', 'Oranges', 'Dates') 

#fruits2= tuple(('Apples', 'Pears', 'Chikoo', 'Oranges', 'Dates'))


fruits2=('Bananas', 'Musk melon', 'Cherries')

print(fruits)

print(fruits, type(fruits))

#Get value
print(fruits[1])

#Can't change value
#fruits[0] = 'Banana'

#delete tuple
del fruits2

#print(fruits2)


#get length
print(len(fruits))



#A set is a collection which is unorderd and unindexed. No duplicate numbers.

#create set
fruits_set = {'Apples', 'Pears', 'Chikoo', 'Oranges', 'Dates'}


#check if in set
print('Apples' in fruits_set)

#add to set
fruits_set.add('Grapes')

#remove from set
fruits_set.remove('Grapes')

print(fruits_set)


#clear set
fruits_set.clear()

#delete set
del fruits_set

print(fruits_set)