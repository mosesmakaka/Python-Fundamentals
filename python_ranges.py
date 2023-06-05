
#range() is a built-in function used to create an immutable sequence of numbers. It is commonly used for looping a specific number of times in for loops.
#range() takes three arguments:
#start: integer starting from which the sequence of integers is to be returned
#stop: integer before which the sequence of integers is to be returned.
#step: integer value which determines the increment between each integer in the sequence
#range() returns a sequence of integers starting from the start integer, goes up to stop - 1, and increments by step. If step is not provided, it defaults to 1.
#range() is a generator, meaning it doesn't create the list of numbers until it is needed. This is why you can't print range(10) directly. You have to convert it to a list first.
#range() is commonly used in for loops to loop a specific number of times. It is also used in list comprehensions to create a list of numbers within a specific range.
#range() is also used in slicing to specify the start, stop, and step arguments.
#range() is also used in the random module to generate a random integer within a specific range.
#range() is also used in the zip() function to iterate over multiple iterables at the same time.
#range() is also used in the enumerate() function to return an index-value pair for each element in an iterable.
#range() is also used in the sorted() function to sort a list of numbers in ascending order.
#range() is also used in the reversed() function to reverse a list of numbers.
#range() is also used in the all() function to check if all elements in an iterable are True.
#range() is also used in the any() function to check if any element in an iterable is True.
#range() is also used in the min() function to return the smallest number in a list of numbers.
#range() is also used in the max() function to return the largest number in a list of numbers.
#range() is also used in the sum() function to return the sum of all numbers in a list of numbers.
#range() is also used in the map() function to apply a function to each element in an iterable.
#range() is also used in the filter() function to filter out elements from an iterable.
#range() is also used in the reduce() function to reduce a list of numbers to a single value.
#range() is also used in the join() function to join a list of strings together.
#range() is also used in the format() function to format a string.
#range() is also used in the print() function to print a list of numbers.
#range() is also used in the input() function to get a list of numbers from the user.
#range() is also used in the open() function to open a file.
#range() is also used in the write() function to write a list of numbers to a file.
#range() is also used in the read() function to read a list of numbers from a file.
#range() is also used in the close() function to close a file.



#range(stop) # This will print a list of numbers from 0 to stop - 1.

#range(start, stop)    # This will print a list of numbers from start to stop - 1. 

#range(start, stop, step)   # This will print a list of numbers from start to stop - 1, incrementing by step.

print(range(10)) # This will only print range(0, 10) because range is a generator.

print(list(range(10))) # This will print a list of numbers from 0 to 9.

print(list(range(5, 10))) # This will print a list of numbers from 5 to 9.

print(list(range(0, 10, 2))) # This will print a list of numbers from 0 to 9, incrementing by 2.

print(list(range(10, 0, -1))) # This will print a list of numbers from 10 to 1, decrementing by 1.

print(list(range(10, 0, -2))) # This will print a list of numbers from 10 to 1, decrementing by 2.

print(list(range(10, 0, 2))) # This will print an empty list because the start is greater than the stop and the step is positive.

print(list(range(0, 10, -2))) # This will print an empty list because the start is less than the stop and the step is negative. You can't increment by -2 if the start is less than the stop.

print(list(range(0, 10, 1))) # This will print an empty list because the step is 0. It can't increment by 0.

print(list(range(0, 0, 1))) # This will print an empty list because the start is 0, the stop is 0, and the step is 1. You can't increment by 1 if the start and stop are the same.

# And Another one.

print(list(range(0, 1, 1))) # This will print a list of numbers from 0 to 0, incrementing by 1.

# And Another one.

print(list(range(0, 1, -1))) # This will print an empty list because the start is 0, the stop is 1, and the step is -1.
