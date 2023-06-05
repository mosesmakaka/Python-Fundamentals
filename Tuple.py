"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry") # Allows duplicates
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # Length of tuple or number of items in tuple.

thistuple = ("apple",) # Tuple with one item. Don't forget the comma!
print(type(thistuple))

#NOT a tuple. This is a string.
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male") # A tuple can contain different data types

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])