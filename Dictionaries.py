### Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered,
# changeable and do not allow duplicates.

# Create a dict
student = {'name':'sam','age': 25,'courses':['math','compsci']}
print(student)

# Print value
print(student['name'])
#print(student['id']) # Shows error key does not exist
# To avoid error use .get() returns none or set default instead of error.

## get()
print(student.get('id'))

# set default
print(student.get('id','Not Found'))

# ADD new key&value
student['id'] = 101
student['name'] = 'Shawn' # also upadtes value

# updates multiple values together
student.update({'name':'vironica','age': 23,'courses':['art','design'],'id': 102})
print(student)

# del
# del student['age'] # Deletes the key value pair
# print(student)

# pop()
print(student.pop('age'))
