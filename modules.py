#A module is basically  a file containing a set of functions to include in your application.
#there are core python modules, modules you can install using pip package manager 
#(including Django) as well as custom modules 


#core modules
#1
import datetime

today =datetime.date.today()

print(today)

#2
import datetime
from datetime import date

today = date.today()

print(today)

#3
import time

timestamp =time.time()

print(timestamp)

#4
import time
from time import time

timestamp =time()

print(timestamp)


#pip modules
from camelcase import CamelCase

c=CamelCase()
print(c.hump('hello there world'))

#Import custom module
import validator
from validator import validate_email

email='test@test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Email is invalid')


