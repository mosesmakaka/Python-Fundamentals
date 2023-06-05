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

#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).
#Remember that the first item has index 0.

#This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
#second to last item has the index -2 etc.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
    
#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.


#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#Convert the tuple into a list, add "orange", and convert it back into a tuple:
#This is the only way to edit a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Remove Items
#Note: You cannot remove items in a tuple.
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple   
#print(thistuple) #this will raise an error because the tuple no longer exists 

#Join Two Tuples
#To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Tuple Methods
#Python has two built-in methods that you can use on tuples.
#Method	Description
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found
