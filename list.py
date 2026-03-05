#List
courses = ['History','Math','Compsci','Physics']
print(courses)

#Length
print(len(courses))

# Returns value by index
print(courses[0])
print(courses[-1])

numbers = [1,2,3,4,5,6,7,8,9,10]
#Slicing
print(numbers[1:3])
print(numbers[1:]) # assumes till end
print(numbers[:2]) # assumes from starting
print(numbers[0:9:2]) # returns every second value from 0th idx to the 9th idx

print(numbers[-7:-2]) #Negative indexing

#Reverse
print(numbers[::-1])

#Method

# append(adds value at the end)
(courses.append('Art'))
print(courses)

# insert(adds value index wise)
(courses.insert(2,'Zoology'))
print(courses)

# extent(adds value at the end just the elements even if its a list, tuple etc)
courses_2 = ['Biology','Media']
courses.append(courses_2) # added the whole list to the list
print(courses)

courses_2 = ['Biology','Media']
courses.extend(courses_2) #added only the elements
print(courses)

# Remove(removes specified values)
courses.remove('Media')
print(courses)

# Pop(removes the end value )
courses.pop()
print(courses)

# Returns popped value
popped = courses.pop()
print(popped)

# index(){Returns the index of the given value}
print(courses.index('Math'))

# In case just to check the existence of the value
print('Art' in courses) # returns True or False

# reverse
courses.reverse()
print(courses)

# sort
courses.sort()
print(courses) # sorts them in aplhabetical order

# To sorted in desc order
# There are two ways
# 1)courses.sort()
#   courses.reverse() 

# other easier option
courses.sort(reverse=True)
print(courses)

# Returns the sorted list without altering the orignal list
sorted_courses = sorted(courses)
print(sorted_courses) 

# Can be printed directly
print(sorted(courses))

# Other Built-in functions
numbers = [1,2,3,4,5,6,7,8,9,10]

# min() Returns the minimum value
print(min(numbers))

# max() Returns the maximum value
print(max(numbers))

#sum() Returns the sum of all the sequence
print(sum(numbers))

#Loop
for course in courses:
    print(course) # By default returns the every value in new line

# Enumerate - returns index with value
for index,course in enumerate(courses):
    print(index,course)

# for starting index with 1 instead of 0
for index,course in enumerate(courses,start=1):
    print(index,course)

# Converts list to a string with chosen seprator
course_str = ' - '.join(courses)
print(course_str)
print(type(course_str))

# Converts string back to list
new_list = course_str.split(' - ')
print(new_list)
print(type(new_list))