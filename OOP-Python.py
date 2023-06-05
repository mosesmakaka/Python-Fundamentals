#Object oriented programming is when you create your own custom class.
#One reason you should do this is that is saves you time.
#Another reason is it makes calling certain functions easier with tkinter
#Another reason is that it makes your code more readable.
#Another reason is that it makes your code more organized.
#Another reason is that it makes your code more efficient.


class Dog:              # Dog is the name of the class
#init creates certain parameters that allow you to define information quickly.
    def __init__(self, name): # this is a constructor
        self.name = name #this is an attribute
    
    def get_name(self): #this is a method
	    return self.name #returns the name of the dog
    
if __name__ == "__main__": #this is a way to run the code in this file only if it is the main file
    d = Dog(str(input("Name your dog: "))) #creates a dog object
    print(d.get_name()) #prints the name of the dog
    print(d.name) #prints the name of the dog
    print(d) #prints the object
    print(type(d)) #prints the type of the object
    print(d.__class__) #prints the class of the object  (same as type(d))
    print(d.__class__.__ne__) #prints the name of the class of the object
    print(d.__dict__) #prints the dictionary of the object
    print(d.__doc__) #prints the docstring of the object
    print(d.__module__) #prints the module of the object
    print(d.__class__.__module__) #prints the module of the class of the object
    print(d.__class__.__module__.__ne__) #prints the name of the module of the class of the object
    print(d.__class__.__module__.__dir__) #prints the directory of the module of the class of the object
    