#A function is a block of code which only runs when it is called.In python, we don't use curly brackets, 
# we use indentation with tabs and spaces.

#create function
def sayHello(name='Sam'):
    print(f'Hello {name}')
    
    
#Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(3,4))


#A lambda function is a small anonymous function
#A lambda function can take any no of arguments,but can only  have one expression. Very similar
#to JS arrow functions


getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 3))


