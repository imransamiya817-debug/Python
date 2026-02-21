#Basic
print("hello world")

#     String
#A String is a collection of individual character
#We can use both single and double quotes with the string
#use single quotes when when you have string like 'world is called as "duniya" in urdu'
#use duble quotes when you have string like "Bobby's world"
#You can also do "world is called as \"duniya\" in urdu" and 'Bobby\'s world'

# SLICING
message = 'hello world'
print(len(message))

#index wise
print(message[0:6])

                  #Method#

#UPPER
print(message.upper())


#Lower
print(message.lower())

#Count
print(message.count('l')) #counts how many time does 'l' came takes char and string as well

#Find
print(message.find('h')) # find the index of given char or str gives startin idx of str

#Replace
print(message.replace('world','Universe'))
print(message)#But its still giving output of hello world why because method
#does not change actual value it returns new value if you want to replace og val
#than just assign it to the variable again
#in python we assign a value to the already assingned variable it deletes the past value and adds new

message = message.replace('world','Universe')
print(message)


#Concatenation
greeting = 'Hello'
name = 'Valerie'

#Can use '+' sign
message = greeting + ', ' + name + ' Welcome!' #can be confusing for long concatenation 
print(message)

#use Format
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(message))#shows all the attributes and methods we can use on the variable

#if want to know more about string function in detail
print(help(str))

# if want to know about specific function
print(help(str.lower))
