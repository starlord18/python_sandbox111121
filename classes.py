#A class is like a blueprint for creating objects. An object has properties and methods(functions)
#associated with it. Almost everything in opython is an object.

#create class
class User:
    #constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        
    #method
    def greeting(self):
        return f'My name is {self.name} and my age is {self.age}'    
    
    #method2
    def has_birthday(self):
        self.age+=1    
        
#Init user object
brad=User('Brad Traversy','brad@gmail.com', 37)
print(type(brad))
print(brad.email)


brad.has_birthday()
print(brad.greeting())


#Extend class
class Customer(User):
    #constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        self.balance=0
        
    def set_balance(self,balance):
        self.balance=balance
        
    def greeting(self):
        return f'My name is {self.name} and my age is {self.age} and my balance is {self.balance}'
    
    
#Init Customer object
janet=Customer('Janet Johnson', 'janet@gmail.com', 25)

janet.set_balance(500)
print(janet.greeting())
    