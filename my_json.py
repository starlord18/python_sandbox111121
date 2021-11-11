#JSON is commonly uesd with data APIs. Here how we can parse json into a python dictionary.

import json

#Sample JSON
userJSON ='{"first_name": "Wasim", "last_name": "Akhtar", "age": 21}'

#Parse to dict
user=json.loads(userJSON)

print(user)

print(user['first_name'])


#parse dictionary to JSON

car={'make': 'Ford', 'model': 'Mustang GT', 'year': 1970}

carJSON=json.dumps(car)
print(carJSON)