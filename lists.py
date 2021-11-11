#create list
numbers1 = [1, 2, 3, 4, 5]

numbers2 = [4, 0, 9, 7]

fruits= ['Apples', 'Oranges', 'Banana', 'Papaya']

#get value
print(fruits[2], numbers1[4])

#get length
print(len(fruits))

#append to list
fruits.append('Mangoes')

print(fruits)

#remove from list
numbers1.remove(3)

print(numbers1)

#Insert into position
fruits.insert(2, 'Strawberry')

print(fruits)


#remove with pop
fruits.pop(3)


#reverse list
fruits.reverse()

print(fruits)


#sort list
fruits.sort()

#reverse sort
fruits.sort(reverse=True)

print(fruits)

#change value
fruits[1] = 'Blueberries'

print(fruits)