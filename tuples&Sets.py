# Tuples (immutable)
# A tuple is similar to a list in Python. 
# Most operations that work on lists also work on tuples, 
# such as indexing, slicing, and iteration.  
# The main difference is that **tuples are immutable**,
# which means their elements cannot be modified after creation.

#### Example
my_tuple = (1, 2, 3, 4)

# Indexing
print(my_tuple[0])   # 1

# Slicing
print(my_tuple[1:3]) # (2, 3)

# Iteration
for item in my_tuple:
    print(item)

# Modification (not allowed)
my_tuple[0] = 10  # Error: tuples are immutable

mytuple = ('CompSci','Math','Physics','History')
print(type(mytuple))
print(mytuple)

# Printing a single value tuple
mytuple1 = ('CompSci')
mytuple2 = ('CompSci',)
print(type(mytuple1))
print(type(mytuple2))

# Once a tuple is created, you cannot change its values.
# But there is a workaround. 
# You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.

#Ex
mytuple = ("Book", "Pen", "Desk")
list_T = list(mytuple)
list_T[1] = "Chair"
list_T.append("Bag")
mytuple = tuple(list_T)

print(mytuple) 

### SETS
myset = {"apple", "banana", "cherry"}

# A set is a collection which is unordered, unchangeable,
# and unindexed. Set items are unchangeable, but you can
# remove items and add new items.

# Creating a empty set
my_set = set()
my_set = {} # It's not correct
print(type(my_set)) # it will be a dictionary

# frozenset 
# It is an immutable version of a set.
# Unlike sets, elements cannot be added or removed from a frozenset.

my_set = frozenset({"apple", "banana", "cherry"})
print(my_set)
print(type(my_set))

# Intersection()
my_set = {'Red','Blue','Green','Orange'}
my_set1 = {'Pink','Red','Green','Purple'}
print(my_set.intersection(my_set1)) # Returns the common value

# difference()
print(my_set.difference(my_set1)) # Returns the uncommon value

# Unionn()
print(my_set.union(my_set1)) # Combines all the values except duplicates
